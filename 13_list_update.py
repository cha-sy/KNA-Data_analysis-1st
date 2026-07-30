# 기존 배열의 모든 요소에 3을 곱한 값을 가진 새 리스트 작성
# 빈 리스트에서 시작해 값 채우기


temps = [25, 26, 24, 28]
doubled = []
for t in temps:
    doubled.append(t * 3)
print(doubled)

# temps = [1, 5, 2, 7, 4, 8, 10, 3]
# high = []
# low = []

# for t in temps:


# 실습 4 조건에 맞는 값으로 새 리스트 만들기
temps = [20, 32, 24, 45, 37, 21, 23, 33]
hot = []
for t in temps:
    if t > 30:
        hot.append(t)
print(hot)  # [32, 35, 31, 33]
print(len(hot))

# 실습 5
temps = [25, 26, 24, 28, 27]
fahrenheit = []
for t in temps:
    fahrenheit.append(t * 1.8 + 32)
print(fahrenheit)


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
