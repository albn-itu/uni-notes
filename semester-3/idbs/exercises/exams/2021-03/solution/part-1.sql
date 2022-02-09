-- a)
SELECT count(*)
FROM vaccines v
JOIN diseases d on d.id = v.disid
WHERE d.name = 'Coronavirus'; -- 3

-- b)
SELECT COUNT(distinct i.peoid)
FROM injections i
JOIN vaccines v on v.id = i.vacid
JOIN diseases d on d.id = v.disid
JOIN categories c on c.id = d.catid
WHERE d.curable AND c.name = 'Bone diseases'; -- 514

-- c)
DROP VIEW IF EXISTS diseaseVaccines;
CREATE VIEW diseaseVaccines AS
SELECT v.id as vid, d.id as did, d.name, v.effectyears
FROM diseases d
JOIN vaccines v on d.id = v.disid;

SELECT v.vid
FROM diseaseVaccines v
WHERE v.name = 'Coronavirus' AND v.effectyears = (
    SELECT MAX(v.effectyears)
    FROM diseaseVaccines v
    WHERE v.name = 'Coronavirus'
); -- 536

-- d)
SELECT COUNT(*)
FROM (
    SELECT d.id
    FROM diseases d
    JOIN vaccines v on d.id = v.disid
    GROUP BY d.id
    HAVING COUNT(distinct v.id) < 5
) X; -- 65

-- e)
SELECT count(distinct i.peoid)
FROM injections i
JOIN vaccines v on v.id = i.vacid
JOIN diseases d on d.id = v.disid
WHERE d.name = 'Coronavirus' AND (i.injectionyear + v.effectyears) >= 2021;

-- f)
SELECT 1.0
    * (SELECT COUNT(*) FROM injections)
    / (SELECT COUNT(*) FROM people); -- 57.490

-- g)
SELECT COUNT(*)
FROM (
    SELECT i.peoid
    FROM injections i
        JOIN vaccines v on v.id = i.vacid
        JOIN diseases d on d.id = v.disid
    GROUP BY i.peoid
    HAVING COUNT(distinct d.catid) = (
        SELECT COUNT(*)
        FROM categories
    )
) X; -- 450

-- h)
DROP VIEW IF EXISTS curableImmuneDiseasesWithCount;
CREATE VIEW curableImmuneDiseasesWithCount AS
SELECT i.peoid, d.id, COUNT(distinct v.id)
FROM injections i
JOIN vaccines v on v.id = i.vacid
JOIN diseases d on d.id = v.disid
JOIN categories c on c.id = d.catid
WHERE c.name = 'Immune diseases' AND d.curable
GROUP BY i.peoid, d.id;

DROP VIEW IF EXISTS maxVaccinesPeople;
CREATE VIEW maxVaccinesPeople AS
SELECT p.id, p.birthyear
FROM curableImmuneDiseasesWithCount c
JOIN people p ON c.peoid = p.id
WHERE c.count = (
    SELECT MAX(c.count)
    FROM curableImmuneDiseasesWithCount c
);

SELECT m.id
FROM maxVaccinesPeople m
WHERE m.birthyear = (
    SELECT MIN(m.birthyear)
    FROM maxVaccinesPeople m
); -- 422