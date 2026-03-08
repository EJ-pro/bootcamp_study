from datetime import datetime, timedelta

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


## 문제: 근무일 계산기 
# 시작일과 종료일을 입력받아 주말과 공휴일을 제외한 실제 근무일을 계산하는 함수를 작성하세요.

def calculate_working_days(start_date, end_date):
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")

    # 총 일수
    # 총 일수는 마지막날 - 시작날 + 1
    total_dt = (end_dt - start_dt).days
    print("총 근무일 : ", total_dt)

    # 주말 수
    week_cnt = 0
    for i in range(total_dt):
        current_date = start_dt + timedelta(days=i)        
        if current_date.weekday() >= 5:  # 주말
            week_cnt += 1

    print("주말 수 : ",week_cnt)

    # 공휴일 수    
    holiday_cnt = 0
    
    holidays = get_holidays_of_2024()

    for i in range(total_dt):
        current_date = start_dt + timedelta(days=i)
        if current_date.strftime("%Y-%m-%d") in holidays:  # 공휴일
            holiday_cnt += 1

    print("공휴일 : ", holiday_cnt)
    
    # 실제 근무일(주말 + 공휴일 제외)
    fact = total_dt - week_cnt - holiday_cnt
    print("실제 근무일 : ", fact)


print("근무시작일 입력하세요 (YYYY-MM-DD): ")
start_date = input()
print("근무종료일 입력하세요 (YYYY-MM-DD): ")
end_date = input()
calculate_working_days(start_date, end_date)