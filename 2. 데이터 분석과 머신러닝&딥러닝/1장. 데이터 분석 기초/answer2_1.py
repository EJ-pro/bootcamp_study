# 1. **DataFrame 생성 및 기본 정보 확인**
#    - 딕셔너리로부터 DataFrame 생성 (8명의 직원 데이터)
#    - 속성: 이름, 나이, 도시, 급여, 부서, 경력
#    - `df.info()`, `df.describe()` 사용하여 데이터 개요 파악

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
    
if __name__ == "__main__":
    print("DataFrame :")
    print(df.head())

    print("\nInfo:")
    df.info()

    print("\nDescribe :")
    print(df.describe())

    print("\nDescribe (all) :")
    print(df.describe(include='all'))
