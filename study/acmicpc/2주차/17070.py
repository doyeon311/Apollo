# 17070
# 파이프 옮기기 1
from collections import deque
import time
import sys

input = sys.stdin.readline

n = int(input())

house = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * n for _ in range(n)] for _ in range(n)]

dp[0][0][1] = 1

for i in range(2, n):
  if house[0][i] == 0:
    dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, n):
  for c in range(1, n):
    if house[r][c] == 0:
      dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1] # 가로
      dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c] # 새로
      if house[r][c - 1] == 0 and house[r - 1][c] == 0: # 대각선
        dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))

# start = time.time()
# move = {
#   "row": [[(0, 1), (0, 1)], [(0, 1), (1, 1)]],
#   "column": [[(1, 0), (1, 0)], [(1, 0), (1, 1)]],
#   "cross": [[(1, 1), (0, 1)], [(1, 1), (1, 0)], [(1, 1), (1, 1)]]
# }
# def check_state(current):
#   block1, block2 = current

#   dx = block2[0] - block1[0]
#   dy = block2[1] - block1[1]
  
#   if dx == 0 and dy == 1:
#     return 'row'
#   elif dx == 1 and dy == 0:
#     return 'column'
#   else:
#     return 'cross'

# def is_movable(current_state, next):
#   block1, block2 = next
#   b1_x, b1_y = block1
#   b2_x, b2_y = block2
#   if current_state == 'cross':
#     for x in range(b1_x, b2_x + 1):
#       for y in range(b1_y, b2_y + 1):
#         if house[x][y] == 1:
#           return False

#   if house[b1_x][b1_y] == 1 or house[b2_x][b2_y] == 1:
#     return False

#   return True

# # 파이프의 한쪽 끝을 N, N으로 이동시킬 수 있는 방법의 수
# result = 0

# dp = [[0] * n for _ in range(n)]

# q = deque()
# q.append([[0, 0], [0, 1]])

# if house[n- 1][n - 1] == 1:
#   print(0)
# else:

#   while q:
#     current = q.popleft()
    
#     if [n - 1, n - 1] in current:
#       result += 1
#       continue
    
#     current_state = check_state(current)

#     for d1, d2 in move[current_state]:
#       block1, block2 = current
#       nb1_x, nb1_y = [block1[0] + d1[0], block1[1] + d1[1]]
#       nb2_x, nb2_y = [block2[0] + d2[0], block2[1] + d2[1]]

#       next = [[nb1_x, nb1_y], [nb2_x, nb2_y]]

#       if 0 <= nb1_x < n and 0 <= nb1_y < n and 0 <= nb2_x < n and 0 <= nb2_y < n:
#         if is_movable(check_state(next), next):
#           # dp[nb1_x][nb1_y] += 1
#           # dp[nb2_x][nb2_y] += 1
#           q.append(next)

#   # end = time.time()

#   print(result)

  # print(f"{end - start:.5f} sec")