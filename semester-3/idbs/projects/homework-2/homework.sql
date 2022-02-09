SELECT COUNT(*)
FROM empires
WHERE empire = 'Danish Empire'; -- 3

SELECT COUNT(distinct c.countrycode)
FROM countries_continents c
    JOIN countries_continents c2 ON c.countrycode = c2.countrycode
WHERE c.continent <> c2.continent AND (c.continent = 'Europe' or c2.continent = 'Europe');

SELECT SUM(population * (cl.percentage / 100))
FROM countries
    JOIN countries_continents cc on countries.code = cc.countrycode
    JOIN countries_languages cl on countries.code = cl.countrycode
WHERE continent = 'South America' AND population > 1000000 AND language = 'Spanish'; -- 160575157

-- Contains repetition of empire = "Benelux"
SELECT distinct COUNT(*) OVER () as count
FROM empires e
    JOIN countries_languages cl on e.countrycode = cl.countrycode
WHERE empire = 'Benelux'
GROUP BY cl.language
HAVING COUNT(*) = (SELECT COUNT(*) FROM empires WHERE empire = 'Benelux')
