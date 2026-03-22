# Seaborn의 iris 데이터를 사용해 아래 요구사항을 모두 충족하는 시각화를 만드세요.

# **지시사항:**

# ##1. 꽃 종류(species) 별로 sepal_length와 sepal_width의 관계를 scatter plot으로 표현하세요.
# 	색상은 species에 따라 다르게 표현
# 	seaborn의 scatterplot 사용
# ##2. sepal_length의 분포를 Histogram + KDE를 함께 나타내는 distplot 또는 displot(seaborn 버전 따라 선택)으로 시각화하세요.
# 	bins 개수는 최소 20 이상 설정
# ##3. 네 가지 특징(sepal_length, sepal_width, petal_length, petal_width) 간의 상관관계를 heatmap으로 시각화하세요.
# 	annot=True 옵션을 사용해 수치를 표시할 것
# 	cmap은 적절한 연속형 팔레트 사용 (예: "Blues", "coolwarm")

# 위 세 그래프는 서브플롯 3개로 구성된 하나의 figure로 나타내세요.

# [출력 형태 예시]
# Fig: scatter plot / distplot(or hist+kde) / heatmap
# 모든 subplot에 제목 포함.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. 데이터 로드
iris = sns.load_dataset('iris')

# 2. Figure 구성 (1행 3열)
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

# ##1. 꽃 종류(species) 별로 sepal_length와 sepal_width의 관계 (Scatter Plot)
sns.scatterplot(
    data=iris, 
    x='sepal_length', 
    y='sepal_width', 
    hue='species', 
    ax=axes[0]
)
axes[0].set_title("Sepal Length vs Width by Species")

# ##2. sepal_length의 분포 (Histogram + KDE)
# sns.histplot은 Histogram과 KDE를 동시에 그리는 현대적인 방법입니다.
sns.histplot(
    data=iris, 
    x='sepal_length', 
    bins=20, 
    kde=True, 
    ax=axes[1],
    color='skyblue'
)
axes[1].set_title("Distribution of Sepal Length")

# ##3. 네 가지 특징 간의 상관관계 (Heatmap)
# 상관계수 계산 (수치형 데이터만 선택하기 위해 species 제외)
corr = iris.drop(columns='species').corr()
sns.heatmap(
    corr, 
    annot=True, 
    cmap='coolwarm', 
    fmt=".2f", 
    ax=axes[2]
)
axes[2].set_title("Feature Correlation Heatmap")

# 레이아웃 조정 및 출력
plt.tight_layout()
plt.show()