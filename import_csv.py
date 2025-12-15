import sqlite3
import csv

conn = sqlite3.connect("medicine.db")
cur = conn.cursor()

with open("data/인천광역시_폐의약품_수거함.csv", encoding="cp949") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        name = row[0]
        address = row[1]

        cur.execute(
            "INSERT INTO box (name, address) VALUES (?, ?)",
            (name, address)
        )

conn.commit()
conn.close()
print("CSV 데이터 저장 완료")