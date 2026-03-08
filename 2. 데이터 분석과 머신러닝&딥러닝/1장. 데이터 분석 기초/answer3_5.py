# 5. **시각화**
#    - 좌석등급별 생존율 막대 그래프
#    - 성별-좌석등급 생존율 히트맵
#    - 연령대별 생존자 수
import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')

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
