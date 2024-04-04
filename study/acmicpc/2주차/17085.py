# 17085
# 십자가 2개 놓기

n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

biggest_cross = min(n, m) - 1 if min(n, m) % 2 == 0 else min(n, m)

cross1 = []
cross2 = []

crosses = []

for x in range(n):
  cross = []
  for y in range(m):
    if board[x][y] == '#':
      cross = [[x, y]]
      crosses.append(cross)
      for size in range(1, biggest_cross // 2 + 1):
        temp_cross = []

        for dx, dy in d:
          nx = x + (dx * size)
          ny = y + (dy * size)
          if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '#':
            temp_cross.append([nx, ny])

        if len(temp_cross) == 4:
          cross = cross + temp_cross
          crosses.append(cross)
        else:
          break

result = 0
def dfs(cross1, cross2, current):
  global result
  if len(cross1) != 0 and len(cross2) != 0:
    result = max(result, len(cross1) * len(cross2))
    return
  
  for i in range(current, len(crosses)):
    if len(cross1) == 0:
      dfs(crosses[i], [], i + 1)
    else:
      flag = True
      for dot in crosses[i]:
        if dot in cross1:
          flag = False
          break
      
      if flag:
        dfs(cross1, crosses[i], i + 1)


for i in range(len(crosses)):
  dfs(crosses[i], [], i + 1)

print(result)