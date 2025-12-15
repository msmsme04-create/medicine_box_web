import sqlite3

conn = sqlite3.connect("medicine.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS box (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    csv_no INTEGER,
    district TEXT,
    name TEXT,
    address TEXT,
    detail TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS report (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    box_id INTEGER,
    content TEXT,
    created_at TEXT
)
""")

conn.commit()
conn.close()

print("DB 생성 완료")