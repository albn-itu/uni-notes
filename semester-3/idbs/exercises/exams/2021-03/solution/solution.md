# 2021-03
## Part 1 (40 points) (Achieved: 30 points)
### a) (5 points) (Achieved: 5 points)
```sql
SELECT count(*)
FROM vaccines v
JOIN diseases d on d.id = v.disid
WHERE d.name = 'Coronavirus'; -- 3
```
Answer: 3

### b) (5 points) (Achieved: 5 points)
```sql
SELECT COUNT(distinct i.peoid)
FROM injections i
JOIN vaccines v on v.id = i.vacid
JOIN diseases d on d.id = v.disid
JOIN categories c on c.id = d.catid
WHERE d.curable AND c.name = 'Bone diseases';
```
Answer: 514

### c) (5 points) (Achieved: 5 points)
```sql
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
);
```
Answer: 536

### d) (5 points) (Achieved: 0 points)
```sql
SELECT COUNT(*)
FROM (
    SELECT d.id
    FROM diseases d
    JOIN vaccines v on d.id = v.disid
    GROUP BY d.id
    HAVING COUNT(distinct v.id) > 5
) X;
```
Answer: 65

### e) (5 points) (Achieved: 5 points)
```sql
SELECT count(distinct i.peoid)
FROM injections i
JOIN vaccines v on v.id = i.vacid
JOIN diseases d on d.id = v.disid
WHERE d.name = 'Coronavirus' AND (i.injectionyear + v.effectyears) >= 2021;
```
Answer: 235


### f) (5 points) (Achieved: 0 points)
```sql
SELECT 1.0
    * (SELECT COUNT(*) FROM injections)
    / (SELECT COUNT(*) FROM people);
```
Answer: 57.490


### g) (5 points) (Achieved: 5 points)
```sql
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
) X;
```
Answer: 450 

### h) (5 points) (Achieved: 5 points)
```sql
-- This is massively over complicated, and probably slow as heck, but i am limited by my lack of understanding of what i am doing

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
);
```
Answer: 422

## Part 2 (5 points) (Achieved: 5 points)
a) true (correct 33%)
b) false (correct)
c) true, as we don't insert data yet (correct 33%)
d) false (correct)
e) true (correct 33%)

## Part 4 (25 points) (Achieved: 15 points)
### a) (5 points) (Achieved: 0 points)
a) true (wrong)
b) false (correct)
c) true (wrong)
d) false (wrong)
e) false (wrong)
f) false (wrong)

### b) (5 points) (Achieved: 5 points)
```sql
CREATE SCHEMA IF NOT EXISTS part4;
SET SEARCH_PATH TO part4;

DROP TABLE IF EXISTS Grades;
DROP TABLE IF EXISTS Examiner;
DROP TABLE IF EXISTS Takes;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Term;

CREATE TABLE Term (
    TID SERIAL PRIMARY KEY,
    description VARCHAR NOT NULL
);

CREATE TABLE Student (
    SID SERIAL PRIMARY KEY,
    startsIn INTEGER NOT NULL REFERENCES Term -- StartsIn relation
);

CREATE TABLE Course (
    CID SERIAL PRIMARY KEY
);

CREATE TABLE Takes (
    SID INTEGER NOT NULL REFERENCES Student,
    CID INTEGER REFERENCES Course,
    TID INTEGER REFERENCES Term,
    room VARCHAR NOT NULL,
    PRIMARY KEY (SID, CID, TID)
);

CREATE TABLE Examiner (
    EID SERIAL PRIMARY KEY
);

CREATE TABLE Grades (
    EID INTEGER REFERENCES Examiner,
    SID INTEGER NOT NULL REFERENCES Student,
    CID INTEGER REFERENCES Course,
    TID INTEGER REFERENCES Term,
    FOREIGN KEY (SID, CID, TID)
        REFERENCES Takes(SID, CID, TID),
    PRIMARY KEY (EID, SID, CID, TID)
);
```

### c) (5 points) (Achieved: 5 points)
[./er.png](er.png)

### d) (5 points) (Achieved: 5 points)
a) true (correct 50%)
b) false, its redundant (correct)
c) false (correct)
d) true (correct 50%)

### e) (5 points) (Achieved: 0 points)
```
DE -> AB (BCNF)
A -> C (BCNF)
B -> D (BCNF)
```

## Part 5 (10 points) (Achieved: 6.25 points)
Q1) b (or d) (correct)
Q2) c (correct)
Q3) e, maybe, otherwise no index (it was no index 50% correct)
Q4) f (wrong)

## Part 6 (10 points) (Achieved: 7,5 points)
### a) (5 points) (Achieved: 2,5 points)
a) false, can be optimistic (wrong)
b) false (correct)
c) true (wrong)
d) true (correct 50%)

### b) (5 points) (Achieved: 5 points)
A static data system would be optimal. Specifically what is called a CDN (Content Delivery Network), as it has to be fast at reads, but as the data is static the writes don't matter. A transactional system, while fast at reading is also focused on writing. On top of that most transactional systems, such as PostGres is tuple based, and this workload would in essence only have 1 tuple type, so it would simply not be underused for the job.

## Part 7 (10 points) (Achieved: 7,5 points)
### a) (5 points) (Achieved: 5 points)
a) false (correct)
b) true (correct 50%)
c) false, it could be bad data (correct)
d) true, it allows for memory sharing (correct 50%)

### b) (5 points) (Achieved: 2,5 points)
An SSD is much faster at random reads. Therefore the part that benefits the most is reading the data from the old data structure, as the data can be scattered, so when searching for the right brick to place in the new data structure an SSD would be much faster than the Sequential read based HDD.

