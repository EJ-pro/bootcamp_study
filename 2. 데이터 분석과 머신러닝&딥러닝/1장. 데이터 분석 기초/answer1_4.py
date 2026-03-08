# 4. 조건부 인덱싱
#    - 배열 data = [1, 5, 3, 8, 2, 9, 4, 7, 6]
#    - 5보다 큰 값 추출
#    - 3 이상 7 이하 값 추출
#    - 짝수 값 추출

import numpy as np

data = np.array([1, 5, 3, 8, 2, 9, 4, 7, 6])
q1 = data[data > 5]

q2 = data[(3 < data) & (data < 7)]

q3 = data[data%2 == 0]

print("5보다 큰수 : ", q1)
print("3이상 7이하 : ", q2)
print("짝수만 출력 : ", q3)