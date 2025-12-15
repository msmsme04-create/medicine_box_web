# init_db.py (수정 버전)
import sqlite3
import csv  # 엑셀 파일(CSV)을 읽기 위한 도구

connection = sqlite3.connect('medicine.db')
cursor = connection.cursor()

# 1. 기존 테이블 삭제하고 새로 만들기 (초기화)
cursor.execute("DROP TABLE IF EXISTS bins")
cursor.execute('''
    CREATE TABLE bins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        description TEXT
    )
''')

# 2. CSV 파일 열기
# 주의: 파일이 안 열리면 encoding='utf-8' 부분을 encoding='cp949'로 바꿔보세요.
try:
    with open('data.csv', 'r', encoding='cp949') as file: 
        reader = csv.reader(file)
        next(reader)  # 첫 번째 줄(제목 줄: 약국명, 주소 등)은 건너뛰기

        # 한 줄씩 읽어서 데이터베이스에 넣기
        for row in reader:
           
            name_data = row[0]      # 엑셀의 첫 번째 칸 (약국 이름)
            address_data = row[1]   # 엑셀의 두 번째 칸 (주소)
            
            # 설명 칸이 없으면 '공공데이터'라고 자동으로 적어줌
            cursor.execute("INSERT INTO bins (name, address, description) VALUES (?, ?, ?)",
                        (name_data, address_data, '공공데이터'))
            
    print("CSV 파일의 데이터를 성공적으로 넣었어요!")

except FileNotFoundError:
    print("오류: data.csv 파일을 찾을 수 없어요. 폴더 위치를 확인하세요!")
except Exception as e:
    print(f"오류가 발생했어요: {e}")

connection.commit()
connection.close()