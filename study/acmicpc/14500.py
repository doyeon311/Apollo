# 테트로미노
# 정사각형 4개를 이어붙인 도형
# 인접한 칸으로 4번 이동하면 되지 않나

import sys

def input():
  return sys.stdin.readline()

n, m = map(int, input().split())

board = []
putted = []
max_item = 0
for _ in range(n):
  row = list(map(int, input().split()))
  max_item = max(max_item, max(row))
  board.append(row)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_score = 0

def is_putted(putted, current):
  x, y = current

  for put in putted:
    px, py = put
    if px == x and py == y:
      return True

  return False

def put_tetromino(putted, score):
  global max_score
  if len(putted) == 4:
    max_score = max(max_score, score)
    return

  # 더 진행해도 의미 없으면 return
  if max_score > score + max_item * (4 - len(putted)):
    return

  for put in putted:
    x, y = put
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < n and 0 <= ny < m and is_putted(putted, [nx, ny]) == False:
        put_tetromino(putted + [[nx, ny]], score + board[nx][ny])


for i in range(n):
  for j in range(m):
    put_tetromino([[i, j]], board[i][j])
    
print(max_score)