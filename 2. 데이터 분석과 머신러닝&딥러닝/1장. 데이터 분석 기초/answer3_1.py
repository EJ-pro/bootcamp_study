import seaborn as sns

# 1. **Titanic 데이터셋 이해**
#    - seaborn 라이브러리로 titanic 데이터 로드: `sns.load_dataset('titanic')`
#    - 데이터 형태: 891행, 15개 열
#    - 주요 열: PassengerId, Survived, Pclass, Age, Sex, Fare, Embarked 등
#    - 결측값 확인: Age(177개), Cabin(687개), Embarked(2개) 결측

#    - seaborn 라이브러리로 titanic 데이터 로드: `sns.load_dataset('titanic')`
titanic = sns.load_dataset('titanic')

#    - 데이터 형태: 891행, 15개 열
print("데이터셋 형태:", titanic.shape)

#    - 주요 열: PassengerId, Survived, Pclass, Age, Sex, Fare, Embarked 등
print("주요 열:", titanic.columns)

#    - 결측값 확인: Age(177개), Cabin(687개), Embarked(2개) 결측
print("결측값 개수:\n", titanic.isnull().sum())
