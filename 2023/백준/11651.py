# 좌표 정렬하기 2
import sys

def input():
  return sys.stdin.readline()

n = int(input())

# y가 증가하는 순 -> x가 증가하는 순
points = []
for _ in range(n):
  point = list(map(int, input().split()))
  points.append(point)

points.sort(key=lambda x: (x[1], x[0]))

for x, y in points:
  print(x, y)