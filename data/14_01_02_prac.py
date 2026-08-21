# 실습 1 value_counts로 빈도 세기
import pandas as pd

df = pd.read_csv("14_hydraulic.csv")

print("설비별 빈도")
print(df["설비"].value_counts())

# 교대별 개수
print("\n교대별 빈도")
print(df["교대"].value_counts())

# 실습 2 비율과 불균형 데이터
print("합격 / 불합격 개수")
print(df["판정"].value_counts())

print("\n합격 / 불합격 비율")
print(df["판정"].value_counts(normalize=True).round(3))

# 실습 3 구간으로 묶어 세기
print("진동 최솟값:", df["진동"].min())
print("진동 최댓값:", df["진동"].max())

vibration_level = pd.cut(
    df["진동"], bins=[0, 0.5, 1.0, 2.0], labels=["약함", "보통", "강함"]
)

print("\n진동 구간별 빈도")
print(vibration_level.value_counts())

# 실습 4 groupby로 그룹 집계
print("라인별 평균 압력")
print(df.groupby("라인")["압력"].mean().round(2))

# 2. 설비별 최고 온도
print("\n설비별 최고 온도")
print(df.groupby("설비")["온도"].max())

# 3. 교대별 측정 건수
print("\n교대별 측정 건수")
print(df.groupby("교대").size())
