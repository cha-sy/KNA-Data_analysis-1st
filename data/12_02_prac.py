# 실습 1 head·tail로 디지털 신호 살펴보기
import pandas as pd

df = pd.read_csv("metro_digital_sample.csv")

print("데이터 크기:", df.shape)

print("\n===== head() =====")
print(df.head())

print("\n===== tail() =====")
print(df.tail())

print("\n===== head(10) =====")
print(df.head(10))

# 실습 2 head·tail 행 개수 조절
import pandas as pd

df = pd.read_csv("12_metro_compressor.csv")

print("===== head(1) =====")
print(df.head(1))

print("\n===== head(10) =====")
print(df.head(10))

print("\n===== tail(7) =====")
print(df.tail(7))

print("\n===== head(500) =====")
print(df.head(500))

# 실습 3 구조 파악 3종 도구
import pandas as pd

df = pd.read_csv("metro_digital_sample.csv")

print("===== shape =====")
print(df.shape)

print("\n===== columns =====")
print(df.columns)

print("\n===== dtypes =====")
print(df.dtypes)

# 실습 4 열 이름·자료형 점검
import pandas as pd

df = pd.read_csv("12_metro_compressor.csv")

print("===== 자료형 확인 =====")
print(df.dtypes)

print("\n===== 숫자형 열 =====")
print(df.select_dtypes(include="number").columns)

print("\n===== 문자형 열 =====")
print(df.select_dtypes(include="object").columns)

# 실습 5 info로 데이터 건강검진
import pandas as pd

df = pd.read_csv("metro_digital_sample.csv")

print("===== 데이터 건강검진 =====")
df.info()

print("\n===== 열별 결측 개수 =====")
print(df.isna().sum())

print("\n===== 결측이 있는 열 =====")
print(df.isna().sum()[df.isna().sum() > 0])
