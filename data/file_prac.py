# 실습 1 open으로 파일 읽기

file = open("sensors.txt", "r", encoding="utf-8")

data = file.read()

print("=== read() 결과 ===")
print(data)

file.seek(0)

lines = file.readlines()

print("\n=== readlines() 결과 ===")
print(lines)

file.close()

# 실습 2 with open으로 파일에 쓰기

with open("sensors.txt", "w", encoding="utf-8") as file:
    file.write("안녕하세요.\n")
    file.write("파이썬 실습입니다.\n")
    file.write("with open을 사용하면 자동으로 파일이 닫힘")

with open("sensors.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# 실습 3 a 모드로 기록 이어붙이기

with open("sensors.txt", "a", encoding="utf-8") as file:
    file.write("\n오늘은 a 모드를 연습")
    file.write("\n기존 내용은 그대로 유지")

with open("sensors.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# 실습 4 csv.reader로 CSV 읽기

# # ① csv 모듈을 import
# import os
# import csv

# csv_path = os.path.join(os.getcwd(), "edu", "data", "08_press.csv")

# # ② with open으로 CSV를 읽기 모드 utf-8로 열기

# with open(csv_path, "r", encoding="utf-8") as f:
#     # ③ csv.reader로 reader 객체를 만들기
#     reader = csv.reader(f)
#     # ④ for로 각 행(리스트)을 하나씩 꺼내 출력
#     for row in reader:
#         print(f"각 행 출력 : {row}")


# 실습 5 csv.writer로 csv쓰기
import csv

with open("sensors_data.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["센서명", "측정값"])

    writer.writerow(["온도", 78])
    writer.writerow(["압력", 95])
    writer.writerow(["진동", 0.5])

print("CSV 파일 저장 완료!")

실습 6 csv읽어 조건 저장하기
import csv

result = []

with open("sensors.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        if float(row[1]) > 90:
            result.append(row)

with open("high_sensors.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["센서명", "측정값"])

    writer.writerows(result)

print("90 초과 데이터가 high_sensor.csv에 저장되었습니다.")
