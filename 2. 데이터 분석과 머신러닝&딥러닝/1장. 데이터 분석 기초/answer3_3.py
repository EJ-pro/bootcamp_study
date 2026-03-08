
# 3. **성별-좌석등급별 다중 집계**
#    - `groupby(['sex', 'pclass']).agg()` 사용
#    - 각 그룹별 나이 평균, 요금 최대값, 생존율 계산
#    - 가장 높은 생존율 그룹 찾기
import seaborn as sns
titanic = sns.load_dataset('titanic')
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
