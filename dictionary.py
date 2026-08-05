# 리스트로 크루 여러분의 이름을 나열해봅시다
data_class_list = ["태구", "수진", "영주"]

# 딕셔너리로 정확하게 역할까지 부여해봅시다
data_class_dict = {"반장": "태구", "부반장": "수진", "당번": "영주"}

# 센서로 부터 얻는 예시 데이터로 딕셔너리를 만들어봅시다
sensors = {"센서이름": "보일러", "모터온도": 78, "진동": 0.5}
print(sensors)
print(type(sensors))  # 딕셔너리 타입 확인
empty = {}  # 빈 딕셔너리 생성
print(type(empty))  # 딕셔너리 타입 확인

print(sensors["센서이름"])
print(sensors["모터온도"])
print(sensors["진동"])

# 기존에 있던 key의 값을 변경
sensors["센서이름"] = "펌프"  # 센서이름 값 변경
sensors["진동"] = 0.7  # 진동 값 변경

# 기존에 없던 key의 값을 추가
sensors["펌프압력"] = 95
sensors["유량"] = 42

# 더 이상 필요없는 key와 그 value을 삭제
del sensors["펌프압력"]
del sensors["모터온도"]

print(sensors)

# print(sensors["모터온도"]) # 더 이상 없는 key를 호출하면 에러 발생

print(sensors.get("센서이름"))
print(sensors.get("모터온도"))  # 더 이상 없는 key를 호출하면 None 반환

# motor_degree에는 숫자가 담길거라 생각했는데...
motor_degree = sensors.get("모터온도", 0)

# motor_degree에 숫자가 안담기면 에러 발생
next_degree = motor_degree + 10
print(next_degree)

is_motor_degree_key = "모터온도" in sensors
print(is_motor_degree_key)

if is_motor_degree_key:
    print("그런 키 있어요!")
else:
    print("그런 키 없어요!")

# 위 코드는 이렇게 보통 쓰인다
if "모터온도" in sensors:
    print("그런 키 있어요!")
else:
    print("그런 키 없어요!")

# keys를 가져와봅시다
print(sensors.keys())
# values를 가져와봅시다.
print(sensors.values())
# len을 통해 몇개의 key-value 조합들이 있는지 살펴봅시다
print(len(sensors))

if len(sensors) < 5:
    print("내용이 부족해요!")

for key, value in sensors.items():
    print(key)
    print(value)

# 위와같이 사용하기 보다는, 의미있는 이름으로 사용하기도 한다
for name, value in sensors.items():
    print(name)
    print(value)

# 재미난 사례를 추가로 만들어봅시다
# 나라 이름들로 정리해봅시다
# 유럽 : 스페인(ESP), 프랑스(FRA), 독일(GER), 스위스(SUI), 네덜란드(NED)
# 아시아 : 한국(KOR), 일본(JPN), 중국(CHN), 사우디(SAU), 이란(IRN)
# 남미 : 아르헨티나(ARG), 브라질(BRA), 칠레(CHI), 콜롬비아(COL), 우루과이(URU)
# 각 나라마다 이름과 약칭으로 정리 가능합니다

korea = {"국가명": "대한민국", "약칭": "KOR"}
japan = {"국가명": "일본", "약칭": "JPN"}

# 아시아 나라들을 하나의 리스트로 모아봅시다
asia = [korea, japan]
print(asia)

# 유럽 나라들을 하나의 리스트로 모아봅시다
europe = [
    {"국가명": "스페인", "약칭": "ESP"},
    {"국가명": "프랑스", "약칭": "FRA"},
    {"국가명": "독일", "약칭": "GER"},
    {"국가명": "스위스", "약칭": "SUI"},
    {"국가명": "네덜란드", "약칭": "NED"},
]
print(europe)

for country in europe:
    print(country.get("국가명", "없음"))

    for key, value in country.items():
        print(f"{key}: {value}")

# 여러분의 조별과제
# 포켓몬 1,2,3 진화단계들을 딕셔너리로 만들고
# 그 포켓몬 딕셔너리들이 최소 10개 모인 배열을 만들어봅시다
# 그 배열 데이터를 화면에 print 합니다
# 가능하면 그 배열의 데이터들을 for-in을 사용해서 하나씩 꺼내 print 합시다 (선택사항)
# 다 되면 저 불러주세요!

# 두 딕셔너리를 key-value 조합으로 하나씩 꺼내어 비교하기!
# 다음의 두 딕셔너리는 같은 key들을 가지고 있습니다.
# 측정 데이터
values = {
    "모터온도": 95,
    "진동": 0.5,
    "압력": 88,
}
# 임계치 데이터
limits = {"모터온도": 90, "압력": 90}

for name, value in values.items():
    print(f"{name} : {value}")

    # limits 딕셔너리에도 name의 key가 있다면, 가져와서 비교하자!
    limit_value = limits.get(name, 0)

    if value > limit_value:
        print(name, "경고")


sensors = {"모터온도": 78, "진동": 0.5}
new_data = {"모터온도": 80, "유량": 42}
sensors.update(new_data)  # 기존 딕셔너리에 새로운 딕셔너리의 key-value 조합을 추가
print(sensors)  # 결과: {'모터온도': 80, '진동': 0.5, '유량': 42}


# zip으로 key들의 배열과 value들의 배열을 묶어서 새로운 딕셔너리를 만들 수 있습니다.
# key들과 value들의 숫자를 맞추는 것부터 잘 해야합니다.
names = ["모터온도", "진동", "압력"]
values = [78, 0.5, 95]
sensors = dict(
    zip(names, values)
)  # zip 기능으로 두 배열을 사용해 묶고 dict 타입 딕셔너리로 만들기
print(sensors)  # 결과: {'모터온도': 78, '진동': 0.5, '압력': 95}

# 딕셔너리 안에 value로 리스트도 가능합니다.
idols = {
    "BTS": ["RM", "진", "슈가", "제이홉", "지민", "뷔", "정국"],
    "블랙핑크": ["지수", "제니", "로제", "리사"],
    "뉴진스": ["민지", "하니", "다니엘", "해린", "혜인"],
}

my_classroom = {"학년": 3, "반": 1, "반장": "홍길동", "부반장": ["고길동", "둘리"]}

my_school = [
    {"학년": 3, "반": 1, "반장": "홍길동", "부반장": ["고길동", "둘리"]},
    {"학년": 3, "반": 2, "반장": "메타몽", "부반장": ["고라파덕", "피카츄"]},
]

# 딕셔너리 안에 value로 딕셔너리를 사용하기
kbo = [
    {
        "구단명": "삼성",
        "마스코트": "라이온스",
        "구장": {"1구장": "대구라이온스파크", "2구장": "포항야구장"},
    },
    {
        "구단명": "두산",
        "마스코트": "베어스",
        "구장": {"1구장": "잠실야구장", "2구장": "베어스파크"},
    },
]

# 쉽게 배열 안에 딕셔너리 안에 딕셔너리 접근하기
print(kbo[0]["구장"]["2구장"])  # 포항야구장

# 실습 1. 딕셔너리 만들고 다루기

# 1) 센서명을 키(key), 측정값을 값(value)으로 딕셔너리 저장
sensors = {"모터온도": 78, "진동": 0.5}

# 2) 키로 값을 꺼내고 새 키로 추가, 기존 키로 수정
print(sensors["진동"])  # 값 꺼내기
print(sensors.get("진동", 0))  # 값 더 안전하게 꺼내기

sensors["압력"] = 95  # 없던 키를 언급하면 추가
sensors["진동"] = 0.3  # 있던 키를 언급하면 수정

print(sensors)

# 3) get으로 없는 키를 기본값으로 조회, in으로 키 존재 확인
print(sensors.get("면적", -1))  # 면적 key는 존재하지 않아서 -1로 대체
print("진동" in sensors)  # 존재하는 key
print("면적" in sensors)  # 존재하지 않는 key
