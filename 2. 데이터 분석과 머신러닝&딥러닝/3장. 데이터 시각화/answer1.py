# **지시사항:**
##1. Gapminder 데이터셋을 불러오고, 2007년도 데이터만 필터링하세요.
##2. 2007년 데이터를 활용하여 아래 그래프를 하나의 Figure 안에 2개의 subplot으로 구성하세요.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from gapminder import gapminder

# 1. Gapminder 데이터셋 불러오기
df = gapminder.copy()
# 2007년 데이터만 필터링
df2007 = df[df['year'] == 2007]

# 2. Figure 구성
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# --- (1) 서브플롯 1: 산점도 ---
sns.scatterplot(
    data=df2007, 
    x='gdpPercap', 
    y='lifeExp', 
    hue='continent', 
    size='pop', 
    sizes=(20, 1000), 
    alpha=0.7, 
    ax=axes[0]
)
axes[0].set_title("Life Expectancy vs GDP per Capita (2007)")
axes[0].set_xlabel("GDP per Capita")
axes[0].set_ylabel("Life Expectancy")
axes[0].legend(title="Continent / Pop Size", bbox_to_anchor=(1.05, 1), loc='upper left')

# --- (2) 서브플롯 2: 대륙별 평균 수명 막대 그래프 ---
continent_mean = df2007.groupby('continent')['lifeExp'].mean().reset_index()

bar_plot = sns.barplot(
    data=continent_mean, 
    x='continent', 
    y='lifeExp', 
    palette='Set2', 
    ax=axes[1]
)
axes[1].set_title("Average Life Expectancy by Continent (2007)")
axes[1].set_xlabel("Continent")
axes[1].set_ylabel("Average Life Expectancy")

# 각 막대 위에 평균 수명 값을 텍스트로 표시
for p in bar_plot.patches:
    bar_plot.annotate(
        format(p.get_height(), '.1f'), 
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha='center', va='center', 
        xytext=(0, 9), 
        textcoords='offset points'
    )

# [Figure 전체 조건]
plt.tight_layout()
plt.show()