# 실습 1 단일 조건으로 행 추출하기
import pandas as pd

df = pd.read_csv("casting_log.csv")

condition = df["실린더압력"] >= 230

print("===== 조건 만족 개수 =====")
print(condition.sum())

filtered_df = df[condition]

print("\n===== 추출된 행 =====")
print(filtered_df)

print("\n===== 추출 행 수 =====")
print(len(filtered_df))

# 실습 2 임계값 넘는 설비 골라내기
import pandas as pd

df = pd.read_csv("casting_log.csv")

condition = df["비스킷두께"] >= 16

filtered_df = df[condition]

result = filtered_df[["샷", "비스킷두께"]]

print("===== 비스킷두께 16 이상 =====")
print(result)

print("\n조건 만족 개수:", condition.sum())

# 실습 3 두 조건 묶기
import pandas as pd

df = pd.read_csv("casting_log.csv")

condition1 = df["비스킷두께"] >= 16
condition2 = df["사이클타임"] >= 20

and_condition = condition1 & condition2
and_result = df[and_condition]

or_condition = condition1 | condition2
or_result = df[or_condition]

print("===== AND 조건 =====")
print(and_result)
print("AND 조건 만족 개수:", and_condition.sum())

print("\n===== OR 조건 =====")
print(or_result)
print("OR 조건 만족 개수:", or_condition.sum())
