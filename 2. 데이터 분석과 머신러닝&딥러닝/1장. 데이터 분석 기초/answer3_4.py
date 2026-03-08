# 4. **피벗 테이블 생성**
#    - 성별 × 좌석등급 생존율 피벗 테이블
#    - 히트맵으로 시각화하여 패턴 확인
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
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