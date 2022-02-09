import psycopg2

conn = psycopg2.connect(
        dbname='homework-3',
        user='postgres',
        password='fgk87jka',
        host='localhost',
        options=f'-c search_path=homework-3'
)
cur = conn.cursor()

f = open('queries.sql', 'w')

cur.execute('SELECT * FROM OldRentals;')

for row in cur:
    pid = row[0]
    hid = row[1]
    pn = row[2]
    s = row[3]
    hs = row[4]
    hz = row[5]
    hc = row[6]

    f.write(f"INSERT INTO People (PID, PN) VALUES ({pid}, '{pn}') ON CONFLICT DO NOTHING;\n")
    f.write(f"INSERT INTO Cities (HZ, HC) VALUES ({hz}, '{hc}') ON CONFLICT DO NOTHING;\n")
    f.write(f"INSERT INTO Homes (HID, HZ, HS) VALUES ({hid}, {hz}, '{hs}') ON CONFLICT DO NOTHING;\n")
    f.write(f"INSERT INTO Rentals (PID, HID, S) VALUES ({pid}, {hid}, {s}) ON CONFLICT DO NOTHING;\n\n")


cur.close()
conn.close()
