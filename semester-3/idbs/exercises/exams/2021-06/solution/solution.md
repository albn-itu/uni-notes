# 2021-06
## Part 1 (5 points pr question) (Achieved: 30 points)
### a) (5 points) 
```sql
SELECT count(*)
FROM clubs
JOIN cities c on c.id = clubs.cityid
WHERE c.name = 'London'
```
Answer: 6

### b) (0 points)
```sql
SELECT COUNT(s.playerid)
FROM signedwith s
LEFT JOIN clubs c ON s.clubid = c.id
WHERE c.id IS NULL;
```
Answer: 17

### c) (5 points)
```sql
DROP VIEW IF EXISTS awayWins;
CREATE VIEW awayWins
AS
SELECT c.id, c.name, count(*)
FROM clubs c
    JOIN matches m on c.id = m.awayid
WHERE m.awaywin
GROUP BY c.id;

-- Assignment
SELECT count(*)
FROM awayWins a
WHERE a.count = (
    SELECT max(a.count)
    FROM awaywins a
);
```
Answer: 2

### d) (0 points)
```sql
SELECT sum(m.homegoals)
FROM players p
    JOIN signedwith s on p.id = s.playerid
    JOIN matches m on s.seasonid = m.seasonid AND m.homeid = s.clubid
WHERE p.name = 'Steven Gerrard';
```
Answer: 112

### e) (5 points)
```sql
DROP VIEW IF EXISTS clubSignsCount;
CREATE VIEW clubSignsCount AS
SELECT p.id, p.name, count(distinct s.clubid)
FROM players p
JOIN signedwith s on p.id = s.playerid
GROUP BY p.id;

SELECT c.name
FROM clubSignsCount c
WHERE c.count = (
    SELECT MAX(c.count)
    FROM clubSignsCount c
);
```
Answer: Ruud van Nistelrooy

### f) (5 points)
```sql
SELECT COUNT(*)
FROM (
        SELECT p.id
        FROM players p
        EXCEPT
        SELECT DISTINCT s.playerid
        FROM clubs c
        JOIN cities c2 on c2.id = c.cityid
        JOIN signedwith s on c.id = s.clubid
        WHERE c2.name = 'London'
) f;
```
Answer: 22

### g) (5 points)
```sql
select count(*)
from (
    select M.awayID, M.seasonID, count(distinct M.homeID)
    -- Get all matches where the home team is from London
    from matches M
        join clubs C on M.homeID = C.ID
        join cities T on C.cityID = T.ID
    where T.name = 'London'
      -- Get all matches where the home team is from London, and the away team won
      and M.awaywin
    -- Group by the away team and season
    group by M.awayID, M.seasonID
    -- Since the home teams are all from london, if we count the amount of matches left with them
    -- The must have been wins, meaning the away team sent all the londoners home, if the count of home ids
    -- is the same as the amount of london clubs
    having count(distinct M.homeID) = (
        -- Get all London clubs
        select count(*)
        from clubs C
        join cities T on C.cityID = T.ID
        where T.name = 'London'
    )
) X
```
Answer: 2

### h) (5 points)
```sql
DROP VIEW IF EXISTS points;
CREATE VIEW points AS
SELECT m.homeid as clubid, 3 as points, m.seasonid
FROM matches m
WHERE m.homegoals > m.awaygoals
UNION ALL
SELECT m.homeid as clubid, 1 as points, m.seasonid
FROM matches m
WHERE m.homegoals = m.awaygoals
UNION ALL
SELECT m.awayid as clubid, 3 as points, m.seasonid
FROM matches m
WHERE m.homegoals < m.awaygoals
UNION ALL
SELECT m.awayid as clubid, 1 as points, m.seasonid
FROM matches m
WHERE m.homegoals = m.awaygoals;

SELECT c.id, c.name, SUM(p.points)
FROM points p
JOIN clubs c ON c.id = p.clubid
WHERE p.seasonid = 2035
GROUP BY c.id
ORDER BY SUM(p.points) DESC;
```

## Part 2 (5 points) (Achieved: 5 points)
a) true (correct, 33%)
b) false, should be a before trigger (correct)
c) true, it will error but not fail (correct 33%)
d) true (correct 33%)
e) false, it wil update the returned data, but not the record. (correct)

## Part 3

## Part 4 (25 points) (Achieved: 23.33)
### a) (5 points) (Achieved: 3.333 points)
a) false (wrong)
b) true (correct 33%)
c) true (wrong)
d) true, it has to have at least one and at most 1 (correct 33%)
e) false (correct)
f) true, it would have to have its own key (wrong)

### b) (5 points) (Achieved: 5 points)
```sql
CREATE SCHEMA IF NOT EXISTS part4;

SET SEARCH_PATH TO part4;

-- Ordered this way as the depend on each other
DROP TABLE IF EXISTS E4;
DROP TABLE IF EXISTS E5;
DROP TABLE IF EXISTS R3;
DROP TABLE IF EXISTS E3;
DROP TABLE IF EXISTS E1;
DROP TABLE IF EXISTS E2;

CREATE TABLE E2 ( -- correct
    E2ID SERIAL PRIMARY KEY
);

CREATE TABLE E1 ( -- correct
    E1ID SERIAL PRIMARY KEY,
    E2ID INTEGER NOT NULL REFERENCES E2 -- R1
);

CREATE TABLE E3 ( -- correct
    E3ID SERIAL PRIMARY KEY,
    E1ID INTEGER NOT NULL REFERENCES E1 -- R4
);

CREATE TABLE R3 ( -- correct
    E1ID INTEGER NOT NULL REFERENCES E1, -- Interpreted as: REFERENCES R1
    E3ID INTEGER NOT NULL REFERENCES E3 -- Interpreted as : REFERENCES R4
);

CREATE TABLE E5 ( -- correct
    E5ID SERIAL PRIMARY KEY
);

CREATE TABLE E4 ( -- correct
    E4ID SERIAL PRIMARY KEY,
    E5ID INTEGER REFERENCES E5 -- R3
);
```

### c) (5 points) (Achieved: 5 points)
[./er.png](Er diagram)

### d) (5 points) (Achieved: 5 points)
a) false (correct)
b) true (correct 50%)
c) false (correct)
d) true (correct 50%)

### e) (5 points) (Achieved: 5 points)
```
NO -> P
NO -> L
NO -> M
M -> M
N -> M
O -> P
O -> L
```
- Remove M -> M
- NO -> M = N -> M
- NO -> P = O -> P
- NO -> L = O -> L

```
NO
N -> M
O -> PL
```

## Part 5 (10 points) (Achieved: 6.66 points)
### a) (3.33 points) (Achieved: 2.2 points)
query 1) A clustered index would have no effect, as group by does not react to indexing (wrong, a clustered index reads in sorted order, appartently)
query 2) A clustered index on customerid would have a positive effect (correct)
query 3) A clustered index on itemid would have a positive effect (correct)

### b) (3.33 points) (Achieved: 1.1 points)
query 1) A covering index would still have no effect as the group by destroys any hope of profits. (wrong, it would read the minimal number of columns, as sorted)
query 2) A covering index could be defined, but i don't think it would have as big of an effect as just the clustered index. (Wrong, Reads fever columns than clusted)
query 3) Don't, a covering index is almost never a good idea on wildcard select queries (Correct)

### c) (3.33 points) (Achieved: 3.33 points)
The item id. I believe the item id would have more data of it, but also the customer id query would still have to find the max date in the query, where the item id is a simple select query, so i believe that query would be significantly helped by a covering index.

## Part 6 (10 points) (Achieved: 5 points)
### a) (5 points) (Achieved: 2.5 points)
An HDD can only process one query at a time, but it doesn't really have a queue built in, so to ensure that the DBMS can process multiple queries while waiting for the disk, it contains a buffer manager which acts as a queue for incoming requests.

### b) (5 points) (Achieved: 2.5 points)
a) true (correct 50%)
b) true (wrong)
c) false (wrong)
d) false (wrong)

## Part 7 (10 points) (Achieved: 10 points)
### a) (5 points) (Achieved: 5 points)
As stated before an HDD can only perform one write operation at a time, so writing immediatly would be able to stop a previous write operation, which would could break the data. If you decide to queue it and wait, the entire system would slow to a crawl with very long response times. It would result in a much more durable system, but in general not a good idea.

### b) (5 points) (Achieved: 5 points)
a) true (correct 50%)
b) true (correct 50%)
c) false (correct)
d) false (correct)
