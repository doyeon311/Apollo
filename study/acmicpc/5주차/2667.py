# 2667
# 단지번호붙이기

n = int(input())

board = []
for _ in range(n):
  row = list(map(int, list(input())))
  board.append(row)

visited = [[False] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
  q = [(x, y)]
  cnt = 1
  while q:
    current = q.pop(0)
    for i in range(4):
      nx = current[0] + dx[i]
      ny = current[1] + dy[i]
      if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and visited[nx][ny] == False:
        visited[nx][ny] = True
        q.append([nx, ny])
        cnt += 1
  return cnt

cnts = []
for i in range(n):
  for j in range(n):
    if board[i][j] == 1 and visited[i][j] == False:
      visited[i][j] = True
      cnt = bfs(i, j)
      cnts.append(cnt)

print(len(cnts))

cnts.sort()

for cnt in cnts:
  print(cnt)

