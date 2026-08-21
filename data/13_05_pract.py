# 실습 5 위험 순으로 정렬하기
import pandas as pd

df = pd.read_csv("metro_digital_sample.csv")

sorted_df = df.sort_values("비스킷두께", ascending=False)

top5 = sorted_df.head(5)

print("===== 비스킷두께 상위 5개 =====")
print(top5[["비스킷두께"]])

multi_sorted = df.sort_values(["비스킷두께", "사이클타임"], ascending=[False, False])

print("\n===== 다중 정렬 결과 =====")
print(multi_sorted.head())

print("\n다중 정렬 첫 행 품질등급:", multi_sorted.iloc[0]["품질등급"])

# 실습 6 필터링과 정렬 연결
import pandas as pd

df = pd.read_csv("metro_digital_sample.csv")

fault = df[df["품질등급"] == "불량"]

top5_fault = fault.sort_values("비스킷두께", ascending=False).head(5)

print("===== 고장 설비 중 위험 상위 5개 =====")
print(top5_fault[["샷", "비스킷두께"]])
