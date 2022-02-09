-- a)
SELECT count(*)
FROM clubs
JOIN cities c on c.id = clubs.cityid
WHERE c.name = 'London';

-- b)
SELECT COUNT(s.playerid)
FROM signedwith s
LEFT JOIN clubs c ON s.clubid = c.id
WHERE c.id IS NULL;

-- c)
DROP VIEW IF EXISTS awayWins;
CREATE VIEW awayWins
AS
SELECT c.id, c.name, count(*)
FROM clubs c
    JOIN matches m on c.id = m.awayid
WHERE m.awaywin
GROUP BY c.id;

-- Check
SELECT *
FROM awayWins a
WHERE a.name = 'Liverpool';

SELECT max(a.count)
FROM awayWins a;

-- Assignment
SELECT count(*)
FROM awayWins a
WHERE a.count = (
    SELECT max(a.count)
    FROM awaywins a
); -- 2

-- d)
SELECT sum(m.homegoals)
FROM players p
    JOIN signedwith s on p.id = s.playerid
    JOIN matches m on s.seasonid = m.seasonid AND m.homeid = s.clubid
WHERE p.name = 'Steven Gerrard';

-- e)
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

-- f)
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

-- g)
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
) X;

-- h)
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