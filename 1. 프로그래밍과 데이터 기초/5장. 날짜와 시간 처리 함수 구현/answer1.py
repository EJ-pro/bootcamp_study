from datetime import datetime

def validate_date(date_str:str, format="%Y-%m-%d") -> bool:
    """날짜 형식 검증"""
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False


def get_weekday_name(index:int) -> str:
    """한국어 요일/월 이름"""
    WEEKDAY_NAMES = ["월", "화", "수", "목", "금", "토", "일"]
    return WEEKDAY_NAMES[index]

def get_holidays_of_2024() -> dict:
    """한국 공휴일 (2024년)"""
    return {
        "2024-01-01": "신정", "2024-02-16": "설날", "2024-02-17": "설날", "2024-02-18": "설날",
        "2024-03-01": "삼일절", "2024-03-02": "삼일절 대체공휴일", "2024-05-05": "어린이날",
        "2024-05-24": "부처님 오신 날", "2024-05-25": "부처님 오신 날 대체공휴일",
        "2024-06-03": "제9회 전국동시지방선거", "2024-06-06": "현충일", "2024-08-15": "광복절", "2024-08-17": "광복절 대체공휴일",
        "2024-10-03": "개천절", "2024-10-05": "개천절 대체공휴일", "2024-10-09": "한글날", "2024-12-25": "크리스마스"
    }


## 문제: 나이 계산기 
# 생년월일을 입력받아 현재 나이(만 나이)와 다양한 정보를 출력하는 함수를 작성하세요.

def calculate_age_info(birth_date):
    birth_dt = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()
    # 만나이 계산
    # 만나이 = 현재 연도 - 태어난 연도 (생일 지나면 X 안지나면 -1 )
    age = today.year - birth_dt.year
    if(today.month < birth_dt.month):
        age -= 1
    elif(today.month == birth_dt.month and today.day < birth_dt.day):
        age -= 1
    print("만나이 : ",age)

    #태어난 요일
    #월요일 = 0 일요일 = 7
    week_index = birth_dt.weekday()
    week_name = get_weekday_name(week_index)
    print("태어난 요일 : ",week_name)

    #살아온 총 일수
    total_day = (today - birth_dt).days
    print("살아온 총 일수 : ",total_day)

    #올해의 생일 통과 유무
    # 현재달이  생일달 보다 작으면 통과 X
    # 현재달과 생일달이 같으면 일수를 비교
    if(today.month < birth_dt.month):
        print("생일 통과 : X")
    elif(today.month == birth_dt.month and today.day < birth_dt.day):
        print("생일 통과 : X")
    else:
        print("생일 통과 : O")

print("생년월일을 입력하세요 (YYYY-MM-DD): ")
birth_date = input()
calculate_age_info(birth_date)