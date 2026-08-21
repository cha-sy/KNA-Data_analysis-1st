# 실습 4 groupby로 그룹 집계
import pandas as pd

df = pd.read_csv("equipment_sensor.csv")

line_pressure = df.groupby("라인")["압력"].mean().round(2)
print("라인별 평균 압력")
print(line_pressure)

equipment_temp = df.groupby("설비")["온도"].max()
print("\n설비별 최고 온도")
print(equipment_temp)

shift_count = df.groupby("교대").size()
print("\n교대별 측정 건수")
print(shift_count)

# 실습 5 그룹별 평균 비교와 정렬
vibration_mean = df.groupby("설비")["진동"].mean().round(2).sort_values(ascending=False)

print("설비별 진동 평균 - 큰 순서")
print(vibration_mean)

# 실습 6 여러 기준 조합 그룹
vibration_mean = df.groupby(["라인", "교대"])["진동"].mean().round(2)

print("라인 × 교대별 진동 평균")
print(vibration_mean)

measurement_count = df.groupby(["라인", "교대"]).size()

print("\n라인 × 교대별 측정 건수")
print(measurement_count)

# 실습 7 빈도와 그룹 집계 종합
print("=== 설비별 구성 ===")
print(df["설비"].value_counts())

print("\n=== 정상 / 고장 비율 ===")
print(df["result"].value_counts(normalize=True).round(3))

failure_df = df[df["result"] == "고장"]

print("\n=== 라인별 고장 건수 ===")
print(failure_df.groupby("라인").size())

print("\n=== 설비별 온도 평균 ===")
print(df.groupby("설비")["온도"].mean().round(2))

print("\n=== 설비별 진동 평균 ===")
print(df.groupby("설비")["진동"].mean().round(2))
