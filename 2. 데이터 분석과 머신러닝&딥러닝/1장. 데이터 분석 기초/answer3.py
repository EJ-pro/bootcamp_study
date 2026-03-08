import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 1. **Titanic 데이터셋 이해**
#    - seaborn 라이브러리로 titanic 데이터 로드: `sns.load_dataset('titanic')`
#    - 데이터 형태: 891행, 15개 열
#    - 주요 열: PassengerId, Survived, Pclass, Age, Sex, Fare, Embarked 등
#    - 결측값 확인: Age(177개), Cabin(687개), Embarked(2개) 결측

#    - seaborn 라이브러리로 titanic 데이터 로드: `sns.load_dataset('titanic')`
titanic = sns.load_dataset('titanic')
df = pd.DataFrame(titanic)

#    - 데이터 형태: 891행, 15개 열
print("데이터셋 형태:", df.shape)

#    - 주요 열: PassengerId, Survived, Pclass, Age, Sex, Fare, Embarked 등
print("주요 열:", df.columns)

#    - 결측값 확인: Age(177개), Cabin(687개), Embarked(2개) 결측
print("결측값 개수:\n", df.isnull().sum())

# 2. **좌석 등급별 생존율 분석**
#    - `groupby('pclass')['survived'].mean()` 사용
#    - 예상 결과: 1등석 > 2등석 > 3등석 생존율
#    - 생존율 차이 해석

survival_rate_by_class = titanic.groupby('pclass')['survived'].mean()
print("좌석 등급별 생존율:\n", survival_rate_by_class)
# 생존율 차이 해석
print("\n생존율 차이 해석:")
print(f"1등석 승객은 {survival_rate_by_class.iloc[0]*100:.2f}%가 생존했으며, 2등석 승객은 {survival_rate_by_class.iloc[1]*100:.2f}%가 생존했습니다. 반면, 3등석 승객은 {survival_rate_by_class.iloc[2]*100:.2f}%만이 생존했습니다.")

# 3. **성별-좌석등급별 다중 집계**
#    - `groupby(['sex', 'pclass']).agg()` 사용
#    - 각 그룹별 나이 평균, 요금 최대값, 생존율 계산
#    - 가장 높은 생존율 그룹 찾기

# groupby(['sex', 'pclass'])로 성별과 좌석 등급별로 그룹화한 후, agg()로 여러 통계량 계산
grouped_stats = titanic.groupby(['sex', 'pclass']).agg({
    'age': 'mean',        # 나이 평균
    'fare': 'max',        # 요금 최대값
    'survived': 'mean'    # 생존율 계산 (0과 1의 평균이 생존율)
}).reset_index()

print("성별-좌석등급별 다중 집계 결과:\n", grouped_stats)
# 가장 높은 생존율 그룹 찾기
highest_survival_group = grouped_stats.loc[grouped_stats['survived'].idxmax()]
print("\n가장 높은 생존율 그룹:")
print(highest_survival_group)

# 4. **피벗 테이블 생성**
#    - 성별 × 좌석등급 생존율 피벗 테이블
#    - 히트맵으로 시각화하여 패턴 확인

# 피벗 테이블 생성
pivot_table = titanic.pivot_table(index='sex', columns='pclass', values='survived', aggfunc='mean')
print("성별 x 좌석등급 생존율 피벗 테이블:\n", pivot_table)
# 히트맵으로 시각화
# seaborn의 heatmap 함수를 사용하여 피벗 테이블 시각화
plt.figure(figsize=(8, 6))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('성별 x 좌석등급 생존율 히트맵')
plt.xlabel('좌석등급 (Pclass)')
plt.ylabel('성별 (Sex)')
plt.show()

# 5. **시각화**
#    - 좌석등급별 생존율 막대 그래프
#    - 성별-좌석등급 생존율 히트맵
#    - 연령대별 생존자 수

# 좌석등급별 생존율 막대 그래프
plt.figure(figsize=(8, 6))
sns.barplot(x='pclass', y='survived', data=titanic, ci=None)
plt.title('좌석등급별 생존율')
plt.xlabel('좌석등급 (Pclass)')
plt.ylabel('생존율 (Survival Rate)')
plt.ylim(0, 1)
plt.show()

# 성별-좌석등급 생존율 히트맵
pivot_table = titanic.pivot_table(index='sex', columns='pclass', values='survived', aggfunc='mean')
plt.figure(figsize=(8, 6))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('성별 x 좌석등급 생존율 히트맵')
plt.xlabel('좌석등급 (Pclass)')
plt.ylabel('성별 (Sex)')
plt.show()

# 연령대별 생존자 수
# 연령대를 10살 단위로 구분하여 생존자 수 계산
titanic['age_group'] = (titanic['age'] // 10) * 10
age_group_survival = titanic.groupby('age_group')['survived'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='age_group', y='survived', data=age_group_survival, ci=None)
plt.title('연령대별 생존자 수')
plt.xlabel('연령대 (Age Group)')
plt.ylabel('생존자 수 (Number of Survivors)')
plt.show()