# 2178
# 미로 탐색
# BFS

n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, list(input()))))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = [[0, 0]]

while q:
  current = q.pop(0)

  if current == [n-1, m-1]:
    break
  
  x, y = current
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny <m and board[nx][ny] == 1:
      board[nx][ny] = board[x][y] + 1
      q.append([nx, ny])

print(board[n-1][m-1])