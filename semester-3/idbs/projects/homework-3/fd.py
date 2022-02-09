import psycopg2

sql = """
SELECT 'Rental: %s --> %s' AS FD,
CASE WHEN COUNT(*)=0 THEN 'MAY HOLD'
ELSE 'does not hold' END AS VALIDITY
FROM (
    SELECT R.%s
    FROM Rentals R
    GROUP BY R.%s
    HAVING COUNT(DISTINCT R.%s) > 1
) X;
"""

conn = psycopg2.connect(
        dbname='homework-3',
        user='postgres',
        password='fgk87jka',
        host='localhost',
        options=f'-c search_path=homework-3'
)
cur = conn.cursor()

def create_sql(att1, att2):
    return sql % (att1, att2, att1, att1, att2)

f = open('out.txt', 'w')
def write_sql(att1, att2):
    cur.execute(create_sql(att1, att2))
    res = cur.fetchone()
    print(res)
    if res[1] == 'MAY HOLD':
        f.write(f'{res[0]} = {res[1]}\n')
    

attrs = ['PID', 'HID', 'PN', 'S', 'HS', 'HZ', 'HC']
for i in range(len(attrs)):
    for j in range(len(attrs)):
        if i != j:
            write_sql(attrs[i], attrs[j])

cur.close()
conn.close()
