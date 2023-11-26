import sqlite3
import Data

# conn = sqlite3.connect("ss.db")
conn = sqlite3.connect(":memory:")

conn.row_factory = sqlite3.Row

Data.InitDB(conn)
Data.CreatePairings(conn)

cursor = conn.cursor()
cursor.execute("""
SELECT s.firstName || ' ' || s.lastName as santaName, s.email AS sEmail, 
t.firstName || ' ' || t.lastName as targetName, t.email as tEmail FROM EventUser AS eu
INNER JOIN Users AS s ON s.id=eu.UserId
INNER JOIN Users AS t on t.id=eu.targetUserId
""")
rows = cursor.fetchall()
i=0
f = open("santa.csv", "w")
for row in rows:
    textRow = f"{row['santaName']}, {row['sEmail']}, {row['targetName']}, {row['tEmail']}\n"
    print(textRow)
    f.write(textRow)
    i += 1

f.close()

print("Done!")
conn.close()
