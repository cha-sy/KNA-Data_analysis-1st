# 실습 6. read_csv 옵션 종합 연습
# G O A L 경로· 인코딩· 구분자· 열 선택을 한 번에 적용

# 세미콜론+한글 파일에서 필요한 열만
# sep + encoding + usecols → 200행 3열

# 여러 옵션을 함께 써서 shape 확인

# -------------------------------------
# 파일 : data 폴더 안의 12_metro_compressor_semicolon.csv
# sep를 잘 사용해서 여러 컬럼이 읽히도록 해주세요
# encoding도 지정해주세요
# 모든 컬럼을 다 읽지는 마시고, '측정시각', '오일온도', '모터전류' 컬럼만 읽어주세요

# ===========================================================================
# 실습 1 head-tail로 디지털 신호 살펴보기
import pandas as pd

# 다음 코드로부터 시작해주세요
df = pd.read_csv("data/12_metro_digital.csv")

# 위 코드가 정상 실행되어 shape가 나오는지 부터 확인하시고
# 적절한 숫자들의 줄을 정해서 .head()와 ,tall()을 출력하세요.

# head와 tall 출력해서 NaN위치가 보이는지도 확인해봅시다

# 이후에 시간이 허락되면 12_metro_small.csv 파일도 같은 확인을 해봅시다
print("데이터 크기:", df.shape)
print("\n===== head() =====")
print(df.head(10))

print("\n===== tail() =====")
print(df.tail(10))

# 실습 3. 구조 파악 3종 도구
# shape · columns · dtypes로 데이터 뼈대 읽기

# 12_metro_digital.csv 읽어와서 DataFrame에 담기
# .shape 출력
# .columns 출력 df.columns.tolist() 도 출력
# .dtypes 출력

import pandas as pd

# CSV 파일 읽어오기
df = pd.read_csv("data/12_metro_digital.csv")

# 1. 데이터 크기 확인
print("===== shape =====")
print(df.shape)

# 2. 열 이름 확인
print("\n===== columns =====")
print(df.columns)

# 3. 열 이름을 리스트로 확인
print("\n===== columns.tolist() =====")
print(df.columns.tolist())

# 4. 데이터 타입 확인
print("\n===== dtypes =====")
print(df.dtypes)
# ----------------------

# 실습 4. 열 이름·자료형 점검

# 12_metro_compressor.csv 읽어와서 DF에 담기
# .columns 출력 df.columns.tolist() 도 출력
# DF의 dtypes 출력

import pandas as pd

# CSV 파일 읽어오기
df = pd.read_csv("data/12_metro_compressor.csv")

# 열 이름 확인
print("===== columns =====")
print(df.columns)

# 열 이름을 리스트 형태로 확인
print("\n===== columns.tolist() =====")
print(df.columns.tolist())

# 데이터 자료형 확인
print("\n===== dtypes =====")
print(df.dtypes)

# 실습 5 info로 데이터 건강검진
# 12_metro_digital.csv 파일을 열어서 DF생성
# DF의 info() 호출 출력
