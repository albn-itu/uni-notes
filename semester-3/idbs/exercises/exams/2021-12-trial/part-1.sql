SELECT COUNT(DISTINCT g.d_id)
FROM ggarments g
JOIN gmadeof m on g.g_id = m.g_id
JOIN gelements e on m.f_id = e.f_id
WHERE m.mo_percentage > 25 AND e.e_element = 'Procrastinium';

-- Incredibly ineffecient, but it works
SELECT COUNT(*)
FROM gdesigners
WHERE d_id NOT IN (
    SELECT g.g_id
    FROM ggarments g
    WHERE g.co_id IS NOT NULL
    UNION ALL
    SELECT g.co_id
    FROM ggarments g
    WHERE g.co_id IS NOT NULL
);

SELECT d_id
FROM ggarments g
GROUP BY d_id
ORDER BY avg(g_price) DESC
LIMIT 1; -- Not a fan of this, but the assignment states that there should only be one row, and removing this line shows that assumption is corred
