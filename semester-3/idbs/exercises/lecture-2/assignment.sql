set schema 'lecture-2';

-- Exercise 1
SELECT name, record
FROM sports
ORDER BY name;

-- Exercise 2
SELECT s.name, count(r.result)
FROM sports s
    JOIN results r on s.id = r.sportid
GROUP BY s.name;

-- also valid:
SELECT DISTINCT s.name
FROM sports s
    JOIN results r on s.id = r.sportid;

-- Exercise 3
SELECT count(distinct peopleid)
FROM results;

-- Exercise 4
SELECT p.id, p.name, count(*)
FROM people p
    JOIN results r on p.id = r.peopleid
GROUP BY p.id
HAVING count(*) >= 20;

-- Exercise 5
SELECT DISTINCT p.id, p.name, g.description
FROM people p
    JOIN results r on p.id = r.peopleid
    JOIN gender g on p.gender = g.gender
    JOIN sports s on r.sportid = s.id
WHERE s.record = r.result;

-- Exercise 6
SELECT s.name, count(*)
FROM sports s
    JOIN (
        SELECT DISTINCT peopleid, sportid, result
        FROM results
    ) r ON r.sportid = s.id
WHERE s.record = r.result
GROUP BY s.name;

-- Exercise 7
SELECT p.id, p.name, MAX(r.result) as best, to_char(MAX(s.record) - MAX(r.result), '0D99') as difference
FROM people p
    JOIN results r on p.id = r.peopleid
    JOIN sports s on r.sportid = s.id
WHERE s.name = 'Triple Jump'
GROUP BY p.id
HAVING COUNT(*) >= 20;

-- Exercise 8
SELECT DISTINCT p.id, p.name, g.description
FROM people p
    JOIN gender g on p.gender = g.gender
    JOIN results r on p.id = r.peopleid
    JOIN competitions c on r.competitionid = c.id
WHERE c.place = 'Hvide Sande'
  AND extract(YEAR FROM c.held) = 2009;

-- Exercise 9
-- https://stackoverflow.com/questions/22339540/return-first-and-last-words-in-a-person-name-postgres
SELECT p.name, g.description, substring(trim(name) FROM '([^ ]+)$') as lastname
FROM people p
    JOIN gender g on p.gender = g.gender
WHERE (substring(trim(p.name) FROM '([^ ]+)$')) LIKE 'J%sen';

-- Exercise 10
SELECT p.name, s.name, r.result, s.record, to_char(r.result / s.record * 100, '999%') as percentage
FROM results r
    JOIN people p on r.peopleid = p.id
    JOIN sports s on s.id = r.sportid
WHERE r.result NOTNULL and s.record NOTNULL;

-- Exercise 11
SELECT count(distinct p.id)
FROM results r
    JOIN people p on p.id = r.peopleid
WHERE r.result ISNULL;

-- Exercise 12
SELECT s.id, s.name, MAX(r.result)
FROM sports s
    JOIN results r on s.id = r.sportid
GROUP BY s.id
ORDER BY s.id;

-- Exercise 13
SELECT p.id, p.name, count(*)
FROM people p
    JOIN results r ON p.id = r.peopleid
    JOIN sports s on r.sportid = s.id
WHERE s.record = r.result
GROUP BY p.id
HAVING COUNT(distinct s.id) >= 2;

-- Exercise 14
