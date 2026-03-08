import math

if __name__ == "__main__":

  points = [(1, 2), (3, 4), (-1, 5), (2, -3), (0, 0), (4, 1), (-2, -2)]
  print(f"주어진 좌표 데이터: {points}")

  print("문제 1. 원점(0, 0)으로부터의 거리가 3 이하인 점들만 필터링")

  # 1번 풀이
  answer = []

  for x, y in points:
    if x**2 + y**2 <= 9:
        answer.append((x, y))

  print(answer)

  print("문제 2. 모든 점을 x축 기준으로 대칭 이동시킨 새로운 좌표 리스트 생성")
  ## 2번 풀이
  answer = []

  for x, y in points:
    answer.append((x, -y))

  print(answer)