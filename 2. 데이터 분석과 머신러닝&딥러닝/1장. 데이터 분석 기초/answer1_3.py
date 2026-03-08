# numpy 라이브러리를 불러온다.
import numpy as np

# 2. 벡터 c를 만든다.
# np.array()를 사용하면 리스트를 "수학적 벡터"로 사용할 수 있다.
c = np.array([3, 4, 5])

# L1 노름 계산
# np.linalg.norm(벡터, 1)
# 두 번째 인자 1은 "L1 노름을 계산하라"는 의미이다.
# L1 노름 공식: |3| + |4| + |5|
l1_norm = np.linalg.norm(c, 1)


# L2 노름 계산
# np.linalg.norm(벡터, 2)
# 두 번째 인자 2는 "L2 노름을 계산하라"는 의미이다.
# L2 노름 공식: √(3² + 4² + 5²)
l2_norm = np.linalg.norm(c, 2)


# L∞ 노름 계산
# np.linalg.norm(벡터, np.inf)
# np.inf는 "무한대"를 의미한다.
# 이는 L∞ 노름을 계산하라는 뜻이다.
# L∞ 공식: 값들 중 절댓값이 가장 큰 것
linf_norm = np.linalg.norm(c, np.inf)

# 계산된 값을 화면에 출력한다.
print("L1 노름:", l1_norm)
print("L2 노름:", l2_norm)
print("L∞ 노름:", linf_norm)