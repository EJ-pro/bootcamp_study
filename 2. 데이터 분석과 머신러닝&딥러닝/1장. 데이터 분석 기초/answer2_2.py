
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

data = {
        'name': ['김철수', '이영희', '박민수', '최지영', '정태현', '한소희', '윤상호', '배수진'],
        'age': [25, 30, 35, 28, 42, 31, 29, 27],
        'city': ['서울', '부산', '대구', '서울', '광주', '서울', '부산', '대구'],
        'salary': [3500, 4200, 3800, 4500, 5200, 3900, 3600, 4100],
        'department': ['개발', '마케팅', '개발', '기획', '개발', '마케팅', '기획', '개발'],
        'experience': [2, 5, 8, 3, 12, 6, 4, 3]
    }

df = pd.DataFrame(data)

# 2. **단일 조건 필터링**
#    - 나이가 30 이상인 직원 추출
#    - 특정 도시(예: 서울) 거주 직원 찾기
#    - 급여가 4000 이상인 직원 필터링
    
if __name__ == "__main__":
    print("나이가 30 이상인 직원 : ")
    print(df[df['age'] >= 30])

    print("\n서울에 거주하는 직원 : ")
    print(df[df['city'] == '서울'])

    print("\n급여가 4000 이상인 직원 : ")
    print(df[df['salary'] >= 4000])