# 죄표 정렬하기

# n개의 좌표
# 1. x를 오름차순으로 정렬 & 2. y를 오름차순

n = int(input())

points = []

for _ in range(n):
  point = list(map(int, input().split()))
  points.append(point)
  # print(points)

points.sort(key=lambda x: (x[0], x[1]))

# print('result', points)

for point in points:
  print(point[0], point[1])
