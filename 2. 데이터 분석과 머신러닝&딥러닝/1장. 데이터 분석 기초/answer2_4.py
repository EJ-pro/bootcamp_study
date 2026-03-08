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


# 4. **기본 통계 및 집계**
#    - 부서별 평균 급여 계산
#    - 도시별 직원 수
#    - 경력 통계 분석

if __name__ == "__main__":
    print("부서별 평균 급여 : ")
    print(df.groupby('department')['salary'].mean())

    print("\n도시별 직원 수 : ")
    print(df['city'].value_counts())

    print("\n경력 통계 분석 : ")
    print(df['experience'].describe())