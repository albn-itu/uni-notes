SELECT COUNT(*)
FROM cities c
JOIN countries c2 on c2.code = c.countrycode
WHERE c.population > (c2.population / 2);

SELECT COUNT(*)
FROM (
    SELECT SUM(percentage)
    FROM countries c
    LEFT JOIN countries_languages cl on c.code = cl.countrycode
    GROUP BY c.code
    HAVING SUM(percentage) < 100 OR SUM(percentage) IS null
) f;

-- Get country code
SELECT name, code
FROM countries
WHERE name = 'France'; -- FRA

-- Get largest city
CREATE FUNCTION largestCityPop(char(3)) RETURNS integer AS $$
    BEGIN
        RETURN (
            SELECT population
            FROM cities
            WHERE countrycode = $1
            ORDER BY population DESC
            LIMIT 1
        );
    END
$$ LANGUAGE plpgsql;

-- Get smallest city
CREATE FUNCTION smallestCityPop(char(3)) RETURNS integer AS $$
    BEGIN
        RETURN (
            SELECT population
            FROM cities
            WHERE countrycode = $1
            ORDER BY population ASC
            LIMIT 1
        );
    END
$$ LANGUAGE plpgsql;

SELECT c.id, c.population::decimal / smallestCityPop(c.countrycode) as scale
FROM cities c
ORDER BY scale DESC
LIMIT 1;

SELECT countrycode, c2.population / sum(c.population)::decimal as scale
FROM cities c
JOIN countries c2 on c2.code = c.countrycode
WHERE c2.population > 1000000
GROUP BY c.countrycode, c2.population
ORDER BY scale DESC
LIMIT 1;
