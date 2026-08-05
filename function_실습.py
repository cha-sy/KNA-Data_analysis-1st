print(
    "\n===================== 실습 2. 다중 매개변수로 센서값 계산하기 ====================="
)


def station_report(name, temp):
    print(name, temp, "도")


station_report("모터", 78)  # 모터 78 도
station_report("펌프", 92)  # 펌프 92 도


def report2(name, temp):
    print(name + ": " + str(temp))


report2(name="압축기A", temp=75.3)
report2(temp=75.3, name="압축기A")


print(
    "\n===================== 실습 3. 키워드 인자로 함수 호출하기 ====================="
)


def sensor_report(name, temp):
    print(name, temp)


sensor_report(name="모터", temp=78)  # 모터 78
sensor_report(temp=92, name="펌프")  # 펌프 92 (순서를 바꿔도 이름으로 정확히 전달됨)

print(
    "\n===================== 실습 4. 반환값으로 간단 계산기 만들기 ====================="
)


def compute_average(a, b):
    return (a + b) / 2


result = compute_average(80, 90)
print(result)  # 85.0
print(result + 5)  # 90.0 (담은 값을 이어 씀)


def min_max(values):
    return min(values), max(values)


pair = min_max([75.3, 88.0, 49.1])
print(pair)
low, high = min_max([75.3, 88.0, 49.1])
print(low, high)  # 49.1, 88.0


def greet_worker(name):
    print(name + "님 환영합니다")


none_result = greet_worker("작업자")  # 작업자님 환영합니다
print(none_result)  # None

print("\n===================== 실습 5. 센서 통계 함수 만들기 =====================")


def sensor_stats(values):
    return min(values), max(values), sum(values) / len(values)


low2, high2, avg2 = sensor_stats([78, 85, 92])
print(low2, high2, avg2)  # 78 92 85.0


# [개념] 기본값 인자 정의 방법 - 매개변수 뒤에 =값을 적으면 기본값이 정해짐
def report3(name, value, unit="도"):
    print(name + ": " + str(value) + unit)


report3("압축기A", 75.3)  # unit 생략 -> 기본값 "도"
report3("펌프1", 7.2, "bar")  # "bar"로 덮어쓰기


# [개념] 기본값을 덮어쓰기 - 기본값이 있는 매개변수에 인자를 넣으면 기본값은 무시되고 넣은 값이 쓰임
def grade(temp, limit=80):
    if temp > limit:
        return "점검필요"
    return "정상"


print(grade(95, limit=90))  # 키워드로 limit=90 -> 기본값 80 대신 90 사용
