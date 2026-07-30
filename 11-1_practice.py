# for gugu in range(2, 10, 2):
#     if gugu % 2 == 0:
#         print(f"=== {gugu}단 ===")
#         for num in range(1, 10):
#             print(f"{gugu} x {num} = {gugu * num}")
#         print()


# temps = [32, 36, 31]
# total = 0
# count = 0
# for t in temps:
#     if t > 30:
#         total += t
#     count += 1
# print("고온 평균:", total / count)

# 정렬된 배열을 출력하고 싶다면 아래처럼


# 실습 6 센서 데이터 종합 분석하기

temps = [25, 32, 28, 35, 27, 31, 24, 33, 29, 36]

total = 0
for t in temps:
    total += t

print("전체 평균:", total / len(temps))

hot = []
for t in temps:
    if t > 30:
        hot.append(t)

hot_total = 0
for h in hot:
    hot_total += h

print("고온 개수:", len(hot))

hot_average = hot_total / len(hot)
print("고온 평균:", hot_average)

if hot_average > total / len(temps):
    print("고온 평균이 전체 평균보다 높습니다.")
elif hot_average < total / len(temps):
    print("전체 평균이 고온 평균보다 높습니다.")
else:
    print("두 평균이 같습니다.")
