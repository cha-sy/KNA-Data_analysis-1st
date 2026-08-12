# 실습 2

import pandas as pd

df = pd.read_csv("12_metro_compressor.csv")

print(df.head())

# 실습 3
import pandas as pd

df = pd.read_csv("12_metro_compressor.csv", sep=";", encoding="cp949")

print(df.shape)
print(df.head())

# 실습 4
df = pd.read_csv(
    "12_metro_compressor.csv",
    sep=";",
    encoding="cp949",
    usecols=["측정시각", "오일온도", "모터전류", "진동"],
)

print(df.shape)
