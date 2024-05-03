# 쉬운 최단거리
n, m = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

board = []
visited = [[False] * m for _ in range(n)]

dest_x = -1
dest_y = -1
for i in range(n):
  row = list(map(int, input().split()))

  if 2 in row:
    dest_x = i
    dest_y = row.index(2)

  board.append(row)

q = [(dest_x, dest_y)]
board[dest_x][dest_y] = 0
visited[dest_x][dest_y] = True
while q:
  c_x, c_y = q.pop(0)

  for i in range(4):
    x = c_x + dx[i]
    y = c_y + dy[i]

    if 0 <= x < n and 0 <= y < m and board[x][y] == 1 and visited[x][y] == False:
      visited[x][y] = True
      board[x][y] = board[c_x][c_y] + 1
      q.append((x, y))

for i in range(n):
  for j in range(m):
    if not visited[i][j] and board[i][j] != 0:
      print(-1, end=" ")
    else:
      print(board[i][j], end=" ")
  print()

