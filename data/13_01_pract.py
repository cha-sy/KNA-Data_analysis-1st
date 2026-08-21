# 실습 1 데이터 불러오기와 구조 확인하기
import pandas as pd

df = pd.read_csv("sensors.csv")

print("===== 앞 5행 =====")
print(df.head())

print("\n===== 데이터 크기 =====")
print(df.shape)

print("\n===== 열 이름 =====")
print(df.columns)

# 실습 2 열 선택하기
import pandas as pd

df = pd.read_csv("sensors.csv")

temp = df["온도"]
print("===== 단일 열 (Series) =====")
print(temp)

sensor_data = df[["온도", "압력", "진동"]]
print("\n===== 여러 열 (DataFrame) =====")
print(sensor_data)

print("\n===== 평균 =====")
print("온도 평균:", temp.mean())
print("센서 평균:")
print(sensor_data.mean())

# 실습 3 공정 센서 열 골라내기
import pandas as pd

df = pd.read_csv("casting_log.csv")

temp = df["온도"]

print("===== 한 센서 열 =====")
print(temp)
print("자료형:", type(temp))

features = df[["온도", "압력", "진동"]]

print("\n===== 여러 센서 열 =====")
print(features)
print("자료형:", type(features))

print("\n===== 형태 =====")
print(features.shape)

# 실습 4 loc와 iloc로 행 선택하기
import pandas as pd

df = pd.read_csv("casting_log.csv")

print("===== loc 단일 행 =====")
print(df.loc[2])

print("\n===== iloc 단일 행 =====")
print(df.iloc[2])

loc_data = df.loc[2:4]

print("\n===== loc 범위 =====")
print(loc_data)
print("행 개수:", len(loc_data))

iloc_data = df.iloc[2:4]

print("\n===== iloc 범위 =====")
print(iloc_data)
print("행 개수:", len(iloc_data))
