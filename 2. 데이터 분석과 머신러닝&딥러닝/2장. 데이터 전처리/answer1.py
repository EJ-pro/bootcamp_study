import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset('titanic')
df = pd.DataFrame(titanic)

print(df.head())

# 1. 결측값 분석
# 결측값 시각화
# 각 열별 결측값 개수와 비율 확인

print("결측값 개수:\n",df.isnull().sum())
print("결측값 비율:\n",df.isnull().sum() / len(df) * 100)

# 2. 전략1 : 삭제
# df.dropna(subset=['age']) 사용

print("\n전략1 : 삭제")
df1 = df.dropna(subset=['age'])
print("결측값 개수:\n",df1.isnull().sum())

# 3. 전략2 : 대체
# 평균값대체: df.fillna(df.mean())
# 중앙값대체: df.fillna(df.median())
# 최빈값대체: df.fillna(df.mode()[0])

print("\n 평균값 대체")
df2 = df.fillna(df.mean(numeric_only=True))
print("결측값 개수:\n",df2.isnull().sum())

print("\n 중앙값 대체")
df3 = df.fillna(df.median(numeric_only=True))
print("결측값 개수:\n",df3.isnull().sum())

print("\n 최빈값 대체")
df4 = df.fillna(df.mode().iloc[0])
print("결측값 개수:\n",df4.isnull().sum())

# 4. 전략3 : 고급대체
# 성별-좌석 등급별 평균값으로 대체
# 'groupby(['sex', 'pclass']).transform(lambda x: x.fillna(x.mean()))' 사용

print("\n 고급대체")
df5 = df.groupby(['sex', 'pclass'])['age'].transform(lambda x: x.fillna(x.mean()))
print("결측값 개수:\n",df5.isnull().sum())

# 결과비교
# 각 전략별 결측값 개수 확인
# 분포 변화 시각화
# 통계값 비교

print("\n결과비교")
print("각 전략별 결측값 개수:", df1.isnull().sum().sum(), df2.isnull().sum().sum(), df3.isnull().sum().sum(), df4.isnull().sum().sum(), df5.isnull().sum().sum())
print("각 전략별 분포 변화:", df1['age'].describe(), df2['age'].describe(), df3['age'].describe(), df4['age'].describe(), df5.describe())
print("각 전략별 통계값:", df1['age'].mean(), df2['age'].mean(), df3['age'].mean(), df4['age'].mean(), df5.mean())