# 파이썬에서 기본 제공하는 기능들 외에
# 다양한 외부 라이브러리들을 가져오려면
# https://pypi.org/search 사이트에서 검색부터 합시다.


# 터미널에서 바로 pip로 설치를 시도하면 [pip install numpy]
# 전체 시스템에 영향을 주는 설치로 생각되어 거절당한다
# 그래서 개별 working Directory마다 별도의 환경을 구축해
# 그 안에 개별 프로젝트가 사용할 pip 라이브러리들을 따로 받아 쓰게 한다.
# 이 것이 바로 개별환경(venv)

# 1. 현재 경로에 가상환경 생성
# python -m venv .venv

# 2. 가상환경 활성화
# source .venv\scripts\activate
# (이후에는 가상환경 안에서 터미널 명령 실행 가능, pip install numpy)


# 3. (작업/실행 끝나고) 가상환경 종료
# deactivate

import numpy as np

numbers = [1, 2, 3, 4, 5]
# 위 int값들의 리스트를 사용해서 numpy의 배열 만들기

np_numbers = np.array(numbers)
print(np_numbers)

# 소수점 이하가 없는 숫자 타입들로 가득찬 배열
print(np.array[1, 2, 3, 4, 5])  # [1 2 3 4 5]

# 소수점 이하기 았는 숫자 타입들로 가득찬 배열
print(np.array[3.14, 6.7, 7.67])  # [3.14 6.7 7.67]

# 소수점 이하가 있는것 없는것이 섞여있다면?
# 모두 소수점 이하가 있는 것으로 배열 생성
print(np.array[1, 3, 5, 3.14, 6.7, 4])  # [1. 3. 5. 3.14 6.7 4.]

