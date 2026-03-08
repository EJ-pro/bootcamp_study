import math

students = [
    {"name": "김철수", "subjects": {"수학": 85, "영어": 90, "과학": 78}},
    {"name": "이영희", "subjects": {"수학": 92, "영어": 88, "과학": 95}},
    {"name": "박민수", "subjects": {"수학": 78, "영어": 85, "과학": 82}},
    {"name": "정지혜", "subjects": {"수학": 88, "영어": 92, "과학": 89}}
]

def calculate_student_averages(students:list) -> dict:
    answer = []
    for student in students:
        name = student["name"]
        subjects = student["subjects"]
        average = sum(subjects.values()) / 3
        answer.append((name, math.floor(average)))
    averages = dict(answer)
    return averages

print("학생의 평균 점수")
answer = calculate_student_averages(students)
for name, average in answer.items():
    print(f"{name} : {average}점")

def calculate_subject_average(students: list, subject_name: str) -> float:
    scores = []
    for student in students:
        subjects = student["subjects"]
        if subject_name in subjects:
            scores.append(subjects[subject_name])
    if scores:
        return sum(scores) / 4
    else:
        return 0

print("\n과목별 평균 점수")
print("수학 평균:", calculate_subject_average(students, "수학"))
print("영어 평균:", calculate_subject_average(students, "영어"))
print("과학 평균:", calculate_subject_average(students, "과학"))