# 반복문 안에서 예외처리

my_list = ["123", "456", "영크크", "32", "53"]

# 문제 발생경우를 세워봅시다
problems = 0

for text in my_list:
    # 반복을 하는 중에 문제가 생긴 경우만 건너띄고
    # 계속 반복을 이어서 진행시키기
    # my_number = int(test)
    # print(my_number)
    try:
        my_number = int(text)
    except:
        # print("문제발생")
        # 문제가 생겼다면 더 이상 반복문 안의 출력까지 이어가면 안되겠다
        # 그래서 여기서 끊고 다음 내용 처리하게 반복문 넘기기

        # 갈 때 가더라도 문제상항 카운팅 정도는 좋잖아
        problems += 1

        continue

    print(my_number)
print(f"({problems}개는 문제가 있어")

# [실습 2] 반복문에서 불량 줄 건너뛰기
# - 소수점 이하의 숫자가 포함된 숫자들을 20개정도 만들어 배열에 담아주세요
# - 그 사이에 엉뚱한 글자들이 포함한 내용도 포함시켜 주시오. "영크크"
# - 위 리스트 데이터를 사용해서 문제를 풀어주세요

sensor_data = [
    23.5,
    45.8,
    12.3,
    "영크크",
    67.9,
    88.1,
    15.6,
    39.4,
    72.8,
    "영크크",
    91.2,
    10.5,
    54.7,
    31.9,
    48.6,
    "영크크",
    77.3,
    29.8,
    63.1,
    18.4,
    95.7,
    41.2,
    56.9,
]

print("=== 정상 데이터만 출력 ===")

for data in sensor_data:
    if type(data) == str:
        print(f"불량 데이터 발견: {data} → 건너뜀")
        continue

    print(f"측정값: {data}")

# [실습 3] 여러 파일 묶어 처리하기
# - 다음과 같은 식의 리스트를 만들어 반복문으로 처리해봅시다
# - for문으로 리스트의 문자열을 꺼내어 해당 이름의 파일들을 알아보기 시도하면 됩니다

file_names = ["08_string.csv", "09_input.csv", "09_ict_dirty.csv"]

for file_name in file_names:
    print(f"\n===== {file_name} =====")

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError:
        print(f"{file_name} 파일을 찾을 수 없습니다.")
