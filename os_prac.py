print("\n============== 실습 1. import 세 방식으로 모듈 가져오기 =============")
import math

print(math.sqrt(16))  # 4.0
from math import sqrt as square_root

print(square_root(16))  # 4.0
import math as m

print(m.ceil(4.2))  # 5

print("\n========== 실습 2. 표준 라이브러리로 센서값 만들기 ===============")
import random

fake_reading = random.randint(1, 100)
print(fake_reading)  # 예: 57 (실행마다 다름)
print(math.sqrt(fake_reading))  # 그 값의 제곱근

# print("\n============ 실습 4. os로 파일 존재 확인하기 ============")
# target_path = os.path.join(practice_dir, "08_press_sample.csv")
# found = os.path.exists(target_path)
# print(found)  # True
# if found:
#     print("파일 있음")
# else:
#     print("파일 없음")

# missing_path = os.path.join(practice_dir, "08_없는파일.csv")
# print(os.path.exists(missing_path))  # False

# print(
#     "\n=============== 실습 5. datetime으로 점검 기록 남기기 ================"
# )
# file_count = len(os.listdir(practice_dir))
# check_time = datetime.datetime.now()
# print(f"파일 {file_count}개, 점검 시각 {check_time}")


