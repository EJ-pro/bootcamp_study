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

## 문제: 프로젝트 일정 관리기
# 프로젝트 시작일과 소요 기간(근무일 기준)을 입력받아 완료 예정일을 계산하는 함수를 작성하세요.

def calculate_project_schedule(start_date_str, duration_days):
    start_dt = datetime.strptime(start_date_str, "%Y-%m-%d")
    holidays = get_holidays_of_2024()
    
    # 1. 프로젝트 완료 예정일 계산
    # 주말과 공휴일을 제외하고 duration_days만큼 진행
    current_dt = start_dt
    working_days_count = 0
    holiday_count = 0
    
    # 마일스톤을 위한 저장소
    milestones = {0.25: None, 0.50: None, 0.75: None}
    
    while working_days_count < duration_days:
        is_holiday = current_dt.strftime("%Y-%m-%d") in holidays
        is_weekend = current_dt.weekday() >= 5
        
        if not is_holiday and not is_weekend:
            working_days_count += 1
            # 마일스톤 체크 (25%, 50%, 75%)
            for p in milestones:
                if milestones[p] is None and working_days_count >= round(duration_days * p):
                    milestones[p] = current_dt.strftime("%Y-%m-%d")
        elif is_holiday:
            holiday_count += 1
            
        if working_days_count < duration_days:
            current_dt += timedelta(days=1)
            
    finish_day = current_dt.strftime("%Y-%m-%d")
    print("프로젝트 완료 예정일 :", finish_day)
    
    # 2. 소요 근무일
    print("소요 근무일 :", duration_days, "일")
    
    # 3. 총 달력 일수
    total_calendar_days = (current_dt - start_dt).days + 1
    print("총 달력 일수 :", total_calendar_days, "일")
    
    # 4. 프로젝트 기간 중 공휴일 수
    print("공휴일 수 :", holiday_count, "일")
    
    # 5. 마일스톤 날짜들
    print("마일스톤 날짜들 :")
    for p, date in milestones.items():
        print(f"  - {int(p*100)}% 진행 ({date})")


print("프로젝트 시작일 입력하세요 (YYYY-MM-DD): ")
start_date = input().strip()
print("프로젝트 소요 근무일 입력하세요: ")
duration_days = int(input().strip())

calculate_project_schedule(start_date, duration_days)
