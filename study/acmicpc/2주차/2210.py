# 숫자판 점프

# 5x5 숫자판
# 임의의 위치에서 시작해서 인접해있는 네 방향으로 다섯번 이동
# 각 칸에 적혀있는 숫자를 이어붙이면 6자리 수
# 이미 거친 칸 중복 가능
# 000123 가능
# 만들 수 있는 숫자의 가짓수

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

board = []
for _ in range(5):
  row = list(map(int, input().split()))
  board.append(row)

nums = []

def dfs(num_str, current):
  if len(num_str) == 6:
    nums.append(num_str)
    return
  x, y = current

  for i in range(4):
    dx, dy = d[i]

    nx = x + dx
    ny = y + dy
    # print(num_str, current)
    if 0 <= nx < 5 and 0 <= ny < 5:
      current_str = num_str + str(board[nx][ny])
      dfs(current_str, (nx, ny))

for i in range(5):
  for j in range(5):
    dfs(str(board[i][j]), (i, j))
# print(set(nums))
print(len(list(set(nums))))