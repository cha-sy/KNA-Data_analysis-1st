# 실습 1 특정 센서·구간 추출하기
rpm = [1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550]

# 인덱싱: 첫 시점과 마지막 시점 값
first = rpm[0]
last = rpm[-1]

# 슬라이싱: 앞 구간 추출
front = rpm[:4]

# 슬라이싱: 두 칸 간격으로 값 추출
step_two = rpm[::2]

print("첫 시점 값:", first)
print("마지막 시점 값:", last)
print("앞 구간 값:", front)
print("두 칸 간격 값:", step_two)

# 실습 2  행·열 단위로 추출하기
sensors = [[1200, 50], [1350, 55], [1500, 60], [1650, 65]]

equipment = sensors[1]

rpm = [row[0] for row in sensors]

torque = [row[1] for row in sensors]

print("특정 설비 행:", equipment)
print("회전수 열:", rpm)
print("토크 열:", torque)

# 실습 3 센서값 정규화하기
import numpy as np

rpm = np.array([1000, 1200, 1400, 1600, 1800])

min_value = rpm.min()
max_value = rpm.max()

print("최솟값:", min_value)
print("최댓값:", max_value)

normalized = (rpm - min_value) / (max_value - min_value)

print("정규화 배열:", normalized)

# 실습 4 이상 센서값 필터링하기
rpm = np.array([1200, 1500, 1800, 2000, 2200])
torque = np.array([55, 50, 45, 40, 30])

rpm_condition = rpm > 1800

risk_condition = (rpm > 1800) | (torque < 40)

high_rpm = rpm[rpm_condition]
risk_rpm = rpm[risk_condition]
risk_torque = torque[risk_condition]

print("기준 초과 회전수:", high_rpm)
print("위험 조건 회전수:", risk_rpm)
print("위험 조건 토크:", risk_torque)

# 실습 5 조건별 개수와 비율 세기
torque = np.array([30, 45, 50, 55, 60, 35, 40, 25])

condition = torque <= 40

count = condition.sum()

ratio = condition.mean()

print("조건을 만족하는 토크:", torque[condition])
print("조건을 만족하는 개수:", count)
print("전체 대비 비율:", ratio)
print("전체 대비 비율(%):", ratio * 100, "%")

# 실습 6 센서별 기초 통계 구하기
data6 = np.array([[1600, 40.8], [1542, 45.3], [1578, 46.4], [2759, 5.3]])
print(data6)
# [[1600.    40.8]
#  [1542.    45.3]
#  [1578.    46.4]
#  [2759.     5.3]]

# · axis를 열 방향으로 지정해 센서별 평균 계산
print(data6.mean())  # 932.6375
print(np.round(data6.mean(axis=0), 2))  # [1829.5    35.78]

# · 센서별 표준편차 계산
print(np.round(data6.std(axis=0), 2))  # [597.73  18.15]

# [실습 7 코드 라인 설명 주석]
# - np.loadtxt: CSV 파일 데이터를 직접 NumPy 배열로 로드하는 함수입니다.
#   * delimiter=',': 쉼표 구분자
#   * skiprows=1: 맨 윗줄 열 이름(헤더) 1줄 건너뜀
#   * usecols=4: 4번 인덱스 열(회전수) 데이터만 선택 로드
# - 로드된 실데이터의 평균(4212.6), 표준편차(1144.9), 최솟값(58.0), 최댓값(4987.0)을 한 줄로 정량 산출합니다.
# -----------------------------------------------------------------------------
# 실습 7. 파일 데이터로 기초 통계 구하기
# 파일로 저장된 공정 데이터를 불러와 기초 통계 계산

# · np.loadtxt로 회전수 열을 파일에서 불러오기
rpm7 = np.loadtxt(
    "data/10_mct_tool.csv", delimiter=",", skiprows=1, usecols=4, encoding="utf-8"
)

# · 불러온 배열의 평균과 표준편차 계산
print(round(rpm7.mean(), 1))  # 4212.6
print(round(rpm7.std(), 1))  # 1144.9

# · 최솟값과 최댓값으로 값의 범위 확인
print(rpm7.min(), rpm7.max())  # 58.0 4987.0
print(rpm7.max() - rpm7.min())  # 4929.0

# 실습 8. 필터링과 통계 결합하기
# 조건으로 값을 골라낸 뒤 그 값들의 통계 계산

# · 토크 배열 준비
torque8 = np.array([42.8, 46.3, 49.4, 65.7, 41.9, 60.7, 40.2, 4.6])

# · 불리언 인덱싱으로 기준을 넘는 값만 추출
high8 = torque8[torque8 > 50]
print(high8)  # [65.7 60.7]

# · 추출한 값들의 평균과 개수 계산
print(round(high8.mean(), 1))  # 63.2
print(high8.size)  # 2

# 실습 9. NumPy 기초 종합 분석
# 데이터 불러오기, 구조 확인, 필터링, 통계를 하나의 흐름으로 수행

# · np.loadtxt로 회전수와 토크 두 열을 불러오기
data9 = np.loadtxt(
    "data/10_mct_tool.csv", delimiter=",", skiprows=1, usecols=(4, 5), encoding="utf-8"
)
print(data9)

# · shape과 dtype으로 구조 확인
print(data9.shape, data9.dtype)  # (40, 2) float64

# · 회전수가 기준 아래로 떨어진 이상 시점을 필터링해 개수와 평균 계산
rpm9 = data9[:, 0]
print(rpm9)
anomaly = rpm9[rpm9 < 1000]
print(anomaly)  # [58.]
print(anomaly.size, round(anomaly.mean(), 1))  # 1 58.0
