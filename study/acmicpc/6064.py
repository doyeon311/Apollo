# 카잉 달력
import sys

def input():
  return sys.stdin.readline()

MAX_NUM = 1000

t = int(input())

for _ in range(t):
  m, n, x, y = map(int, input().split())

  cnt = 0
  flag = True
  temp = 0
  while temp <= m * n:
    temp = cnt * m + x
    if temp % n == y % n:
      flag = False
      print(temp)
      break
    cnt += 1
  if flag:
    print(-1)