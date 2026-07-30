# while은 특정 조건(횟수 x)이 False가 될 때까지
# 반복 해야 하는 경우 사용

# 무한 루프 유의
# 무한 루프의 강제 종료 : ctrl + c

# while문 사용 체크리스트
# 1. 반복 전 변수(시작값) 존재여부
# 2. 반복을 하다가 언젠가 False가 될 수 있는 종료 조건 포함 여부
# 3. 변수가 거짓 방향으로 값이 변경 되는지

# count = 1

# while count >= 1: #2번
#     # count = 0 # 반복문 안에 count 변수를 계속 0으로 재할당해서 무한루프
#     print(count)
#     count += 1 # 3번

# 실습 1 while로 목표값 도달까지 반복하기

answer = 7
guess = 0
while guess != answer:
    guess = int(input("뭘 까요?!: "))
print("정답입니다!!!")

# 실습 up down 게임
# 1 ~ 50 중 하나의 숫자를 정답으로 저장
# 사용자의 입력값 기준으로 정답이 up인지 down인지 출력
# 정답이 나오면 정답이고, 게임이 종료되었다고 출력

answer = 27

while True:
    my = int(input("하나의 숫자를 입력하시오 (1~50): "))
    if my < answer:
        print("UP")
    elif my > answer:
        print("DOWN")
    else:
        print("정답입니다.")
        print("게임이 종료되었습니다.")
        break

# ==================

# 최댓값 찾기
first = int(input("1번째 입력값: "))

# 첫 번째 입력값은 자동으로 최댓값이 됨(비교할 다른 값이 없기 때문)
max_value = first

# for문을 사용해서 사용자 입력을 4번 받고
# 입력 받은 값 중에서 가장 큰 값을 출력
for i in range(4):
    v = int(input(f"{i + 1}번째 입력: "))

    # max_value에는 현 시점 최댓값
    # v에는 방금 사용자가 입력한 값
    # max_value와 v의 값을 비교해 더 큰 값을 max_value에 재할당
    if v > max_value:
        max_value = v
        print("최댓값:", max_value)  # for 반복문 종료 후 최댓값 출력

# 흐름 표를 보고 코드 작성

values = [4, 7, 6]  # ① 입력
total = 0
count = 0
i = 0
while i < len(values):  # ② 반복
    v = values[i]
    if v > 5:  # ③ 판단
        total += v
        count += 1
    i += 1  # 갱신 - 없으면 무한 루프
print("합계:", total, "개수:", count)  # ④ 출력 -> 13, 2

# 실습 2 플래그로 조건 만족 값 검색하기

m = int(input("횟수: "))
found = False
for i in range(m):
    v = int(input("측정값: "))
    if v > 80:
        found = True
    break
if found:
    print("발견")
else:
    print("없음")

# 실습 1 조건에 맞는 값만 출력하기
temps = [25, 32, 28, 35, 19, 31, 27]
for t in temps:
    if t >= 30:
        print("고온:", t)

# 실습 2 두 조건을 모두 만족하는 값 고르기

hours = [3, 8, 12, 6, 10, 4, 9]
for h in hours:
    if h >= 5 and h <= 10:
        print(h)

# 실습 3 조건에 맞는 값만 골라 평균 구하기

temps = [25, 32, 28, 36, 27, 31, 24]
total = 0
count = 0
for t in temps:
    if t > 30:
        total += t
    count += 1
print("고온 평균:", total / count)
