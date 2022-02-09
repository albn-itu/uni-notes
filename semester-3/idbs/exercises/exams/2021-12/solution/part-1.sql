-- a)
SELECT COUNT(*)
FROM chefs c
WHERE c.id NOT IN (
    SELECT distinct r.created_by
    FROM recipes r
);

-- b)
SELECT COUNT(distinct m.recipe_id)
FROM master m
JOIN recipes r on r.id = m.recipe_id
JOIN use u ON r.id = u.recipe_id
JOIN ingredients i on i.id = u.ingredient_id
JOIN chefs c on c.id = m.chef_id
WHERE i.type = 'spice' AND c.name = 'Spicemaster';

-- c)
SELECT COUNT(*)
FROM (
    SELECT COUNT(step)
    FROM recipes r
    LEFT JOIN steps s on r.id = s.recipe_id
    GROUP BY r.id
    HAVING COUNT(step) <= 3
) X;

-- d)
SELECT COUNT(distinct r.id)
FROM recipes r
JOIN use u ON r.id = u.recipe_id
JOIN ingredients i on i.id = u.ingredient_id
JOIN belong_to bt on i.id = bt.ingredient_id
WHERE r.belong_to = bt.cuisine_id;

-- e)
DROP VIEW IF EXISTS recipeIngredientCount;
CREATE VIEW recipeIngredientCount AS
SELECT r.id, r.name, COUNT(distinct u.ingredient_id) as ingredientCount
FROM recipes r
JOIN use u on r.id = u.recipe_id
JOIN ingredients i on i.id = u.ingredient_id
GROUP BY r.id
ORDER BY ingredientCount DESC;

SELECT r.name
FROM recipeIngredientCount r
WHERE r.ingredientcount = (
    SELECT MAX(r.ingredientcount)
    FROM recipeIngredientCount r
);

-- f)
DROP VIEW IF EXISTS spiceRatio;
CREATE VIEW spiceRatio AS
SELECT b.cuisine_id, 1.0 * SUM(CASE WHEN i.type = 'spice' THEN 1 ELSE 0 END) / COUNT(distinct i.id) as spiceRatio
FROM belong_to b
JOIN ingredients i on i.id = b.ingredient_id
WHERE b.cuisine_id IN (
    SELECT distinct b.cuisine_id
    FROM belong_to b
    JOIN ingredients i2 on i2.id = b.ingredient_id
    WHERE i2.type = 'spice'
)
GROUP BY b.cuisine_id
ORDER BY spiceRatio DESC;

SELECT COUNT(*)
FROM spiceRatio s
WHERE s.spiceRatio = (
    SELECT MIN(s.spiceRatio)
    FROM spiceRatio s
);

-- g)
SELECT COUNT(*)
FROM (
    SELECT u.recipe_id, u.step
    FROM use u
    JOIN ingredients i on i.id = u.ingredient_id
    GROUP BY u.recipe_id, u.step
    HAVING COUNT(distinct i.type) = (
        SELECT COUNT(distinct i.type)
        FROM ingredients i
    )
) X;

-- h)
-- Thai ingredients
DROP VIEW IF EXISTS thaiIngredients;
CREATE VIEW thaiIngredients AS
SELECT distinct b.ingredient_id ingredientId
FROM belong_to b
JOIN cuisines c on c.id = b.cuisine_id
WHERE c.name LIKE '%Thai%';

-- Chefs who have created a recipe in indian cuisine
DROP VIEW IF EXISTS indianCuisineChefs;
CREATE VIEW indianCuisineChefs AS
SELECT distinct r.created_by AS chefId, c.name
FROM recipes r
JOIN cuisines c on c.id = r.belong_to
WHERE c.name LIKE '%Indian%';

SELECT c.id, c.name, SUM(u.quantity) as totalQuantity
FROM chefs c
JOIN recipes r on c.id = r.created_by
JOIN use u on r.id = u.recipe_id
-- Only how chefs who have created cuisine with indian in the name before
WHERE c.id IN (SELECT chefId FROM indianCuisineChefs)
    -- Only factor in ingredients that have Thai in the name
    AND u.ingredient_id IN (SELECT ingredientId from thaiIngredients)
GROUP BY c.id
-- Order by quantity in decreasing order
ORDER BY totalQuantity DESC;


CREATE FUNCTION CheckCousines() RETURNS TRIGGER
AS $$ BEGIN
    IF NOT EXISTS (
        SELECT *
        FROM recipes r
            JOIN belong_to b ON r.belong_to = b.cuisine_id
        WHERE r.id = NEW.recipe_id
            AND b.ingredient_id = NEW.ingredient_id) THEN
        RAISE EXCEPTION 'There is no commom cousine'
        USING ERRCODE = '45000';
    end if;
    RETURN NEW;
END; $$ LANGUAGE plpgsql;

CREATE TRIGGER CheckCousines
    AFTER INSERT ON use
    FOR EACH ROW EXECUTE PROCEDURE checkcousines();

INSERT INTO use(RECIPE_ID, STEP, INGREDIENT_ID, QUANTITY, UNIT) VALUES (1,1,33,-1,'lb');
INSERT INTO use(RECIPE_ID, STEP, INGREDIENT_ID, QUANTITY, UNIT) VALUES (1,1,34,-1,'lb');
INSERT INTO use(RECIPE_ID, STEP, INGREDIENT_ID, QUANTITY, UNIT) VALUES (1,1,34,1,'lb');