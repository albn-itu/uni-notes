# 2021-08
Started: ~19:30
Finished: 21:53
Duration: ~2:30

## Part 1 (5 points pr question) (Achieved: 30 points)
### a) (5 points)
```sql
SELECT COUNT(*)
FROM plants
JOIN families f on f.id = plants.familyid
WHERE f.name = 'Thespesia'; 
```
Answer: 18

### b) (5 points)
```sql
SELECT COUNT(*)
FROM people p
LEFT JOIN plantedin p2 on p.id = p2.planterid
WHERE p2.planterid IS NULL AND position = 'Planter';
```
Answer: 9

### c) (5 points)
```sql
SELECT SUM((p.percentage * 0.01) * f.size)
FROM plantedin p
JOIN flowerbeds f on f.id = p.flowerbedid
JOIN plants p2 on p2.id = p.plantid
JOIN families f2 on f2.id = p2.familyid
WHERE f2.name = 'Vicia';
```
Answer: 27.3

### d) (5 points)
```sql
SELECT p.flowerbedid, SUM(p.percentage)
FROM plantedin p
GROUP BY p.flowerbedid
HAVING SUM(p.percentage) > 100
ORDER BY SUM(p.percentage) DESC;
```
Answer: 243, 51, 51

### e) (0 points)
```sql
SELECT COUNT(*)
FROM (
    SELECT f.id
    FROM flowerbeds f
    LEFT JOIN plantedin p on f.id = p.flowerbedid
    GROUP BY f.id
    HAVING SUM(coalesce(p.percentage)) < 100
) X;
```
Answer: 271

### f) (0 points)
```sql
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
    HAVING SUM(coalesce(p.percentage)) < 100
) X;
```
Answer: 169 

### g) (5 points)
```sql
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
```
Answer: 2

### h) (5 points)
```sql
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
```
Answer: Multiple rows

## Part 2 (5 points) (Achieved: 5)
a) true (correct 33%)
b) false (correct)
c) true (correct 33%)
d) false (correct)
e) true as the first wasn't inserted (correct 33%)

## Part 4 (25 points) (Achieved: 20,5)
### a) (5 points) (Achieved: 3,75)
a) false, attend is 0..n (correct)
b) false (correct)
c) true (correct 25%)
d) true (correct 25%)
e) false (wrong) 
f) true (correct 25%)

### b) (5 points) (Achieved: 5)
```sql
CREATE SCHEMA IF NOT EXISTS part4;
SET SEARCH_PATH TO part4;

DROP TABLE IF EXISTS Attends;
DROP TABLE IF EXISTS Lectures;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Tutor;
DROP TABLE IF EXISTS Censors;
DROP TABLE IF EXISTS Teachers;


CREATE TABLE Teachers (
    TID SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE Censors (
    CID SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE Tutor (
    TuID SERIAL NOT NULL PRIMARY KEY,
    TID INTEGER NOT NULL REFERENCES Teachers(TID),
    CID INTEGER NOT NULL REFERENCES Censors(CID), -- Censor relationship
    fromyear VARCHAR NOT NULL
);

-- Either:
CREATE TABLE Students (
    SID SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    TuID INTEGER NOT NULL REFERENCES Tutor(TuID)
);

-- Or:
-- CREATE TABLE Students (
--     SID SERIAL PRIMARY KEY,
--     name VARCHAR NOT NULL,
--     fromyear VARCHAR NOT NULL,
--     TID INTEGER NOT NULL,
--     CID INTEGER NOT NULL,
--     FOREIGN KEY (TID, CID, fromyear) REFERENCES Tutor(tid, cid, fromyear)
-- );

CREATE TABLE Lectures (
    LID SERIAL PRIMARY KEY,
    subject VARCHAR NOT NULL
);

CREATE TABLE Attends (
    LID INTEGER NOT NULL REFERENCES Lectures(LID),
    SID INTEGER NOT NULL REFERENCES Students(SID),
    PRIMARY KEY (LID, SID)
);
```

### c) (5 points) (Achieved: 5)
[er.png](er.png)

### d) (5 points) (Achieved: 3,333)
a) false (correct)
b) true (correct 33%)
c) false (wrong)
d) true (correct 33%)

### e) (5 points) (Achieved: 3,333)
```
LM -> N
N -> OP
```

## Part 5 (10 points) (Achieved: 10)
### a) (3.333 points) (Achieved: 3,33)
(Q1) A clustered index on objecttypeid would result in large perfomance gain, assuming that objecttypeid 22 has few elements

(Q2) (radius, lat, long) Could result in a perfomance gain, but since it would retrieve half the objects, a clustered index would probably be better.

(Q3) A clustered index on objectID could result in a massive perfomance gain as the retrieved data is stored sorted

### b) (3.333 points) (Achieved: 3,333)
(Q1) A covering index on the whole table is usually a bad idea

(Q2) (radius, Lat, Long) could have a perfomance gain as the number of columns is low, which is good as we are pulling half the tables data.

(Q3) The clustered index above would be prefereable.

### c) (3.333 points) (Achieved: 3,33)
ObjectID has the largest chance of being profitable, but objecttypeid could also result in performance gain. In a real situation it would be prefereable to run benchmarks.

## Part 6 (10 points) (Achieved: 7,5)
### a) (5 points) (Achieved: 5)
STEAL has the advantage of allowing the buffer management system to reuse memory by writing the updated transaction pages directly to the disk. This has the disadvantage of having to remember the old value to undo them. In this server STEAL simply does not apply.

### b) (5 points) (Achieved: 2,5)
a) true, i dont think so tho (wrong)
b) false (correct)
c) false (wrong)
d) true (correct 50%)

## Part 7 (10 points) (Achieved: 7,5)
### a) (5 points) (Achieved: 5)
In ACID the concistency attribute refers to the integrity of the data, such that when a transaction has completed, the integrity of the data is ensured. For example in a relational when inserting data the triggers and foreign keys will be checked and the system will out right block the data if it doesnt uphold the integrity constraints.

### b) (5 points) (Achieved: 2,5)
a) true (correct 50%)
b) true (wrong)
c) false (wrong)
d) false (wrong)

