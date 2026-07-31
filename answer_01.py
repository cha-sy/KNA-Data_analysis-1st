# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)


# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)

# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)

# TODO 4. 전체 평균 온도 출력 (round)

# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)

# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())


# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"

# ===========================================================================
                        # 설비 종합 모니터링 리포트
# ============================================================================
normal_count = 0
caution_count = 0
danger_count = 0

# 평균 온도를 구하기 위한 누적변수
total_temp = 0

# 위험 설비 이름을 저장할 리스트
danger_names = []

# 가장 높은 온도를 찾기 위한 초기값
max_name = sensors[0][0]
max_temp = sensors[0][1]


# 1. 각 설비 상태 판정 + 번호 출력
for i, (name, temp, vibration) in enumerate(sensors, start=1):

    # 온도 > 90 또는 진동 > 5.0이면 위험
    if temp > 90 or vibration > 5.0:
        status = "위험"
        danger_count += 1

        # 위험 설비 이름 저장
        danger_names.append(name)

    # 온도 >= 80 또는 진동 >= 3.0이면 주의
    elif temp >= 80 or vibration >= 3.0:
        status = "주의"
        caution_count += 1

    # 그 외는 정상
    else:
        status = "정상"
        normal_count += 1

    # 온도 누적
    total_temp += temp

    # 가장 높은 온도 직접 찾기
    if temp > max_temp:
        max_temp = temp
        max_name = name

    # 한 줄 출력
    print(f"{i}. {name} - 온도: {temp}°C, 진동: {vibration}, 상태: {status}")


# 2. 정상 / 주의 / 위험 개수 출력
print()
print(f"정상: {normal_count}대")
print(f"주의: {caution_count}대")
print(f"위험: {danger_count}대")


# 3. 이상 설비 비율
abnormal_count = caution_count + danger_count
abnormal_rate = round(abnormal_count / len(sensors) * 100, 1)

print(f"이상 설비 비율: {abnormal_rate}%")


# 4. 전체 평균 온도
average_temp = round(total_temp / len(sensors), 1)

print(f"전체 평균 온도: {average_temp}°C")


# 5. 온도가 가장 높은 설비
print(f"최고 온도 설비: {max_name}, 온도: {max_temp}°C")


# 6. 위험 설비 이름 정렬
danger_names.sort()

print(f"위험 설비: {danger_names}")
