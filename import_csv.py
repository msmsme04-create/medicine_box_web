import sqlite3
import csv

conn = sqlite3.connect("medicine.db")
cur = conn.cursor()

with open("data/data.csv", encoding="cp949") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        cur.execute("""
        INSERT INTO box (csv_no, district, name, address, detail)
        VALUES (?, ?, ?, ?, ?)
        """, (row[0], row[1], row[2], row[3], row[4]))

conn.commit()
conn.close()

print("CSV 저장 완료")