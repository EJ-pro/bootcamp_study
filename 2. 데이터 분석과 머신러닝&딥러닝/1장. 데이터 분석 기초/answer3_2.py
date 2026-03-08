
# 2. **좌석 등급별 생존율 분석**
#    - `groupby('pclass')['survived'].mean()` 사용
#    - 예상 결과: 1등석 > 2등석 > 3등석 생존율
#    - 생존율 차이 해석
import seaborn as sns
titanic = sns.load_dataset('titanic')
survival_rate_by_class = titanic.groupby('pclass')['survived'].mean()
print("좌석 등급별 생존율:\n", survival_rate_by_class)
# 생존율 차이 해석
print("\n생존율 차이 해석:")
print(f"1등석 승객은 {survival_rate_by_class.iloc[0]*100:.2f}%가 생존했으며, 2등석 승객은 {survival_rate_by_class.iloc[1]*100:.2f}%가 생존했습니다. 반면, 3등석 승객은 {survival_rate_by_class.iloc[2]*100:.2f}%만이 생존했습니다.")
