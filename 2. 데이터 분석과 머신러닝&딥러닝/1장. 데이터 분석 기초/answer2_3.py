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

# 3. **복합 조건 필터링**
#    - AND 연산: 서울 거주 **AND** 급여 4000 이상
#    - OR 연산: 개발팀 **OR** 급여 4500 이상
#    - NOT 연산: 개발팀이 아닌 직원
    
if __name__ == "__main__":
    print("서울 거주 AND 급여 4000 이상 : ")
    print(df[(df['city'] == '서울') & (df['salary'] >= 4000)])

    print("\n개발팀 OR 급여 4500 이상 : ")
    print(df[(df['department'] == '개발') | (df['salary'] >= 4500)])

    print("\n개발팀이 아닌 직원 : ")
    print(df[~(df['department'] == '개발')])