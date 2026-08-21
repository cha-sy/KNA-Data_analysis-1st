# 실습 1 value_counts()로 빈도 세기
import pandas as pd

df = pd.read_csv("설비데이터.csv")

print(df.head())

print("설비별 개수")
print(df["설비"].value_counts())

print("교대별 개수")
print(df["교대"].value_counts())

# 실습 2 비율과 불균형 데이터
print("판정별 개수")
print(df["판정"].value_counts())

print("판정별 비율")
print(df["판정"].value_counts(normalize=True).round(3))

# 실습 3 구간으로 묶어 세기
print("진동 최솟값:", df["진동"].min())
print("진동 최댓값:", df["진동"].max())

vib_band = pd.cut(df["진동"], bins=[0, 2, 4, 10], labels=["약함", "보통", "강함"])

print("\n진동 구간별 개수")
print(vib_band.value_counts())

