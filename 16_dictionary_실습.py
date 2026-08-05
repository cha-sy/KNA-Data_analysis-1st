# 실습 1 딕셔너리 만들고 다루기

# 1) 센서명을 키(key), 측정값을 값(value)으로 하는 딕셔너리 저장
sensors = {"모터온도": 78, "진동": 0.5}

# 2) 키로 값을 꺼내고 새 키로 추가, 기존 키로 수정
print(sensors["진동"])  # 값 꺼내기
print(sensors.get("진동", 0))  # 값 더 안전하게 꺼내기

sensors["압력"] = 95  # 없던 키를 언급하면 추가
sensors["진동"] = 0.3  # 있던 키를 언급하면 수정

print(sensors)  # {'모터온도': 78, '진동': 0.3, '압력': 95}

# 3) get으로 없는 키를 기본값으로 조회, in으로 키 존재 확인
print(sensors.get("면적", -1))  # 면적 key는 존재하지 않아서 -1로 대체
print("진동" in sensors)  # 존재하는 key
print("면적" in sensors)  # 존재하지 않는 key

# 실습 2 update로 여러 값 한 번에 갱신하기

sensors = {"온도센서": 78, "진동센서": 2.5}

new_data = {"진동센서": 3.0, "압력센서": 120}

sensors.update(new_data)

del sensors["압력센서"]

print(sensors)
print("센서 수:", len(sensors))


# 실습 3 딕셔너리로 통계 내기

sensors = {"온도": 65, "진동": 70, "압력": 95}

average = sum(sensors.values()) / len(sensors)

print("평균:", round(average, 1))

max_sensor = ""
max_value = 0

for sensor, value in sensors.items():
    if value > max_value:
        max_value = value
        max_sensor = sensor

print("최댓값 센서:", max_sensor, max_value)

# 실습 4 zip으로 센서명 값 매핑하기

sensor_names = ["온도", "진동", "압력"]
sensor_values = [78, 0.5, 95]

sensors = dict(zip(sensor_names, sensor_values))

print(sensors)

for name, value in sensors.items():
    print(name, "-", value)

# 실습 5 임계값으로 경고 센서 분류하기

sensor_values = {"온도": 85, "진동": 2.5, "압력": 90}

limits = {"온도": 80, "진동": 3.0, "압력": 100}
warn_sensors = []

for name, value in sensor_values.items():
    if value > limits[name]:
        warn_sensors.append(name)

print("경고 센서:", warn_sensors)

# 실습 6 중첩 딕셔너리로 설비 관리하기


# 실습 7 표 데이터를 딕셔너리로 변환하기

sensor_data = ["온도,78", "압력,95", "진동,0.5"]

sensors = {}

for data in sensor_data:
    name, value = data.split(",")

    sensors[name] = float(value)

print(sensors)
