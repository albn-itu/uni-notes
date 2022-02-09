-- a)
SELECT COUNT(*)
FROM plants
JOIN families f on f.id = plants.familyid
WHERE f.name = 'Thespesia'; -- 18

-- b)
SELECT COUNT(*)
FROM people p
LEFT JOIN plantedin p2 on p.id = p2.planterid
WHERE p2.planterid IS NULL AND position = 'Planter'; -- 9

-- c)
SELECT SUM((p.percentage * 0.01) * f.size)
FROM plantedin p
JOIN flowerbeds f on f.id = p.flowerbedid
JOIN plants p2 on p2.id = p.plantid
JOIN families f2 on f2.id = p2.familyid
WHERE f2.name = 'Vicia'; -- 27.3

-- d)
SELECT p.flowerbedid
FROM plantedin p
GROUP BY p.flowerbedid
HAVING SUM(p.percentage) > 100
ORDER BY SUM(p.percentage) DESC;

-- e)
SELECT COUNT(*)
FROM (
    SELECT f.id, SUM(coalesce(p.percentage))
    FROM flowerbeds f
    LEFT JOIN plantedin p on f.id = p.flowerbedid
    GROUP BY f.id
    HAVING SUM(p.percentage) < 100
) X; -- 271


-- f)
SELECT COUNT(*)
FROM (
    SELECT f.id
    FROM flowerbeds f
    LEFT JOIN plantedin p on f.id = p.flowerbedid
    WHERE f.id in (
        SELECT DISTINCT p.flowerbedid
        FROM plantedin p
        JOIN plants p2 on p2.id = p.plantid
        JOIN families f2 on f2.id = p2.familyid
        JOIN types t on t.id = f2.typeid
        WHERE t.name = 'shrub'
    )
    GROUP BY f.id
    HAVING SUM(p.percentage) < 100
) X; -- 169

-- g)
SELECT f.id
FROM families f
JOIN plants p on f.id = p.familyid
JOIN plantedin p2 on p.id = p2.plantid
JOIN flowerbeds f2 on f2.id = p2.flowerbedid
GROUP BY f.id
HAVING COUNT(distinct f2.parkid) = (
    SELECT COUNT(*) FROM parks
); -- 354 (Not the answer)

SELECT COUNT(*)
FROM (
    SELECT f.id
    FROM flowerbeds f
    JOIN plantedin p on f.id = p.flowerbedid
    JOIN plants p2 on p2.id = p.plantid
    JOIN families f2 on f2.id = p2.familyid
    GROUP BY f.id
    HAVING COUNT(DISTINCT f2.typeid) = (
        SELECT COUNT(*) FROM types
    )
) X;

-- h)
DROP VIEW IF EXISTS peoplePlantedInFlowerbeds;
CREATE VIEW peoplePlantedInFlowerbeds(id, name, position, bedPercentage, bedSize, bedParkid) AS
SELECT p.id, p.name, p.position, p1.percentage, f.size, f.parkid
FROM people p
JOIN plantedin p1 on p.id = p1.planterid
JOIN flowerbeds f on f.id = p1.flowerbedid;

SELECT p.id, p.name, SUM((0.01 * p.percentage) * p.size) as totalArea
FROM peoplePlantedInFlowerbeds p
WHERE p.id IN (
    SELECT distinct p.id
    FROM peoplePlantedInFlowerbeds p
    JOIN parks p3 on p3.id = p.parkid
    WHERE p.position = 'Planter' AND p3.name = 'Kongens Have'
)
GROUP BY (p.id, p.name)
ORDER BY totalArea DESC;

