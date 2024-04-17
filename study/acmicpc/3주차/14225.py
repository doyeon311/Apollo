# 14225
# 부분수열의 합

n = int(input())
s = list(map(int, input().split()))

board = [False] * (sum(s) + 2)
def dfs(nums, current):
  if current == n:
    board[sum(nums)] = True
    return

  dfs(nums + [s[current]], current + 1)
  dfs(nums, current + 1)

dfs([], 0)

for num, flag in enumerate(board):
  if flag == False:
    print(num)
    break