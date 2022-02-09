-- Exercise 1
SELECT COUNT(*)
FROM person
WHERE height isnull;

-- Exercise 2
SELECT COUNT(*)
FROM (
    SELECT m.id, AVG(p.height)
    FROM movie m
        JOIN involved i on m.id = i.movieid
        JOIN person p on i.personid = p.id
    WHERE p.height NOTNULL
    GROUP BY m.id
    HAVING AVG(p.height) > 190
) as iA;

-- Exercise 3
SELECT COUNT(distinct movieid)
FROM (
    SELECT movieid, genre, COUNT(*) as c
    FROM movie_genre
    GROUP BY movieid, genre
    HAVINg COUNT(*) > 1
) as ia;

-- Exercise 4
SELECT COUNT(DISTINCT personid)
FROM (
    SELECT DISTINCT m.id
    FROM movie m
        JOIN involved i on m.id = i.movieid
        JOIN person p on i.personid = p.id
    WHERE i.role = 'director'
        AND p.name = 'Steven Spielberg'
    ) as movie_ids
    JOIN involved i on movie_ids.id = i.movieid
    JOIN person p ON i.personid = p.id
WHERE i.role = 'actor';

