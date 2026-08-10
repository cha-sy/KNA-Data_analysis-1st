import numpy as np

# 파이썬의 리스트로부터 numpy 배열 만들기
temp = np.array(78.5, 68.8, 73.7)

print(temp)  # [78.5 68.8 73.7] 항목 사이에 콤마 없음 유의

# 배열의 항목들마다 +5씩 더하려면?
# 리스트였다면 for문으로 돌려서 항목마다 직접처리해줬어야함
# Numpy라면 간단하게
print(temp + 5)
