# 실습 1 센서값 배열 만들기
import numpy as np

celsius = np.array([20.0, 25.0, 30.0, 35.0])
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)  # [68. 77. 86. 95.]

# 실습 2 균등 간격 배열 만들기
even_split = np.linspace(0, 100, 5)
print(even_split)  # [  0.  25.  50.  75. 100.]

# 실습 3 측정 시간축 배열 만들기
time_axis = np.arange(0, 20, 5)
print(time_axis)  # [ 0  5 10 15]
time_axis_finer = np.arange(0, 20, 2)  # 간격을 줄이면 시점 개수가 늘어남
print(time_axis_finer)  # [ 0  2  4  6  8 10 12 14 16 18]

# 실습 4 배열 구조 확인하기
equipment_readings = np.array([[65.2, 67.8, 63.1], [70.1, 72.3, 69.8]])
print(equipment_readings.ndim)  # 2
print(equipment_readings.shape)  # (2, 3)
print(equipment_readings.size)  # 6

# 실습 5 자료형 확인과 변환하기
temp_readings = np.array([65.7, 68.3, 71.9])
print(temp_readings.dtype)  # float64
print(temp_readings.astype(int))  # [65 68 71]
