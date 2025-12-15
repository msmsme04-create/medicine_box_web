import sqlite3
import csv

# 1. 데이터베이스 연결
conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()

# 2. 기존 테이블 삭제 후 새로 만들기

cursor.execute("DROP TABLE IF EXISTS bins")
cursor.execute('''
    CREATE TABLE bins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        description TEXT
    )
''')

# 3. CSV 파일 읽기
try:
    
    with open('data.csv', 'r', encoding='cp949') as file:
        reader = csv.reader(file)
        next(reader)  # 제목 줄(첫 번째 줄) 건너뛰기

        for row in reader:
        
            name_val = row[2]       # C열: 기관명칭
            addr_val = row[3]       # D열: 소재지
            desc_val = row[4]       # E열: 세부위치
            
            # 데이터베이스에 집어넣기
            cursor.execute(
                "INSERT INTO bins (name, address, description) VALUES (?, ?, ?)", 
                (name_val, addr_val, desc_val)
            )
            
    print("✅ 데이터베이스에 C열, D열, E열 정보를 모두 넣었습니다!")

except Exception as e:
    print(f"❌ 오류가 났어요: {e}")

conn.commit()
conn.close()