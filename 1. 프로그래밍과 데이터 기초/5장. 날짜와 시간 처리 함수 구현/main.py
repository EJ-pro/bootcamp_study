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



## 문제: 나이 계산기 
# 생년월일을 입력받아 현재 나이(만 나이)와 다양한 정보를 출력하는 함수를 작성하세요.

def calculate_age_info(birth_date):
    birth_dt = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()
    
    # 만 나이 계산
    age = today.year - birth_dt.year - ((today.month, today.day) < (birth_dt.month, birth_dt.day))
    
    # 태어난 요일 계산
    weekday_index = birth_dt.weekday()
    weekday_name = get_weekday_name(weekday_index)
    
    # 살아온 총 일수 계산
    total_days_lived = (today - birth_dt).days
    
    # 올해 생일 통과 유무
    has_passed_birthday = (today.month, today.day) >= (birth_dt.month, birth_dt.day)
    
    return {
        "age": age,
        "weekday": weekday_name,
        "total_days_lived": total_days_lived,
        "has_passed_birthday": has_passed_birthday
    }

print("생년월일을 입력하세요 (YYYY-MM-DD): ")
birth_date = input().strip()

age_info = calculate_age_info(birth_date)
print("만 나이: ", age_info['age'], "세")
print("태어난 요일: ", age_info['weekday'], "요일")
print("살아온 총 일수: ", age_info['total_days_lived'],"일")
print("올해 생일 통과 유무: ", '통과' if age_info['has_passed_birthday'] else '미통과')


## 문제: 근무일 계산기 
#시작일과 종료일을 입력받아 주말과 공휴일을 제외한 실제 근무일을 계산하는 함수를 작성하세요.
def calculate_working_days(start_date, end_date):
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")

    total_days = (end_dt - start_dt).days + 1
    weekend_count = 0
    holiday_count = 0

    holidays = get_holidays_of_2024()

    for i in range(total_days):
        current_date = start_dt + timedelta(days=i)
        if current_date.weekday() >= 5:  # 주말
            weekend_count += 1
        elif current_date.strftime("%Y-%m-%d") in holidays:  # 공휴일
            holiday_count += 1

    working_days = total_days - weekend_count - holiday_count
    return {
        "total_days": total_days,
        "weekend_count": weekend_count,
        "holiday_count": holiday_count,
        "working_days": working_days
    }


print("근무 시작일을 입력하세요 (YYYY-MM-DD): ")
start_date = input().strip()
print("근무 종료일을 입력하세요 (YYYY-MM-DD): ")
end_date = input().strip()

work_info = calculate_working_days(start_date, end_date)
print("총 일수: ", work_info['total_days'], "일")
print("주말 수: ", work_info['weekend_count'], "일")
print("공휴일 수: ", work_info['holiday_count'], "일")
print("실제 근무일: ", work_info['working_days'], "일")

# **출력 예시:**
# - 총 일수
# - 주말 수
# - 공휴일 수
# - 실제 근무일 (주말 + 공휴일 제외)

## 문제: 프로젝트 일정 관리기
프로젝트 시작일과 소요 기간(근무일 기준)을 입력받아 완료 예정일을 계산하는 함수를 작성하세요.

def calculate_project_schedule(start_date, duration_days, holidays=None):
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    current_dt = start_dt
    working_days_count = 0
    holidays = holidays or get_holidays_of_2024()
    while working_days_count < duration_days:
        current_dt += timedelta(days=1)
        if current_dt.weekday() < 5 and current_dt.strftime("%Y-%m-%d") not in holidays:
            working_days_count += 1

    return current_dt.strftime("%Y-%m-%d")

print("프로젝트 시작일 입력하세요 (YYYY-MM-DD): ")
start_date = input().strip()
print("프로젝트 소요 근무일 입력하세요: ")
duration_days = int(input().strip())
project_end_date = calculate_project_schedule(start_date, duration_days)
print("프로젝트 완료 예정일: ", project_end_date)

# **출력 예시:**
# - 프로젝트 완료 예정일
# - 소요 근무일
# - 총 달력 일수
# - 프로젝트 기간 중 공휴일 수
# - 마일스톤 날짜들 (25%, 50%, 75% 진행 시점)