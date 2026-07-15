# 변수 선언 방법
# 변수이름 = 값
# 오른쪽 값을 왼쪽 이름에 "저장"하라는 코드
temp = 36  # 숫자로 저장하고 싶다면 따옴표 금지
name = "센서 A"  # 글자는 무조건 따옴표로 무조건 감싸기

print(temp)  # 36
print("temp")  # temp

# =은 "같다"가 아니라 "저장"하는 것
# 비교는 ==을 사용

# ===================================
print("=====변수 사용 활용=====")

x = 5
# 변수를 "재할당"할 때 변수 기존 자신의 값을 활용할 수 있음
x = x + 5

print(x)  # 10

# y = y+5 # 오류 발생. y가 선언되지 않았기 때문

# ================================================
print("=====재할당======")
print("재할당하기 전 temp:", temp)  # 재할당 하기 전 temp 출력
temp = 15  # 위에서 할당했던 36이라는 값을 15로 재할당(수정)
Temp = 150  # temp와 다은 변수로 동작
print("temp:", temp)
print("Temp:", Temp)

# 재할당은 지금까지 실행된 코드 중 가장 마지막으로 저장된 값이 불려옴
# print(score) # NameError 발생
score = 10
print(score)  # 10
score = 20
score = 30
print(score)  # 30

# ================================
print("=====값 복사=====")

a = 10
b = a  # b변수에는 10이 저장(저장할 떄의 그 순간의 a값을 b에 복사)
a = 100  # a 변수를 재할당해도
print(b)  # 10 b변수의 값은 10이 그대로 유지됨

print("=====여러 변수 한 번에 선언 및 할당======")

# 형식: 변수1, 변수,2,... = 값1,값2,... <변수와 값이 갯수가 같아야 함

width, height = 10, 20  # width는 10 height는 20이 할당됨
print("width:", width, "height:", height)

# x, y, z = 10, 20  # 변수3개, 값2개 > valueError 발생

# ===================================
print("=====주석으로 변수 설명=====")

# temp = 25  # 온도(섭씨)
# count = 3  # 센서 갯수
# temp = 100000000000 #주석처리된 코드는 동작하지 않음
# print(temp)  # 25


# # 실습1
# temp = 25
# print(temp)  # 25
# name = "센서 A"
# print(name)  # 센서 A

# # 실습2
# temp = 30
# print(temp)
# temperature = 25
# print(temperature)

# # 실습3
# my_number = 10
# print(my_number)
# mood = "우울"
# print(mood)

# # 실습4
# age = 29
# label = "내 나이"
# print(label)
# print(age)

# # 실습5
# x = 10
# print(x)  # 10
# x = x + 5
# print(x)  # 15
# x = x * 2
# print(x)  # 30

# # 실습 6
# a = 100
# b = a
# a = 999
# print(a)  # 999
# print(b)  # 100

# 실습7
# print(temp)
temp = 25
print(temp)
score = 90
# print(Score)
print(score)


# 실습8
temp = 25  # 온도(섭씨)
count = 3  # 센서의 갯수
# temp = 100
print(temp)  # 25

# 실습9
x = 5
x = 10
x = x + 1
print(x)

# 실습10
name = "도시"
city = "광양"
print("설비")
print(name)
print(city)

# 실습11
# a = 12, b = 13
device_temp = 25
sensor_count = 3
print(device_temp)  # 25
print(sensor_count)  # 3

# 실습12
x, y, z = 1, 2, 3
width, height = 4, 3
print(width)  # 4
print(height)  # 3

