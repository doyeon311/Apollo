# 12996
# acka

s, a, b, c = map(int, input().split())

dp = [[[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

def go(total, a, b, c):
  if total == 0:
    if a == 0 and b == 0 and c == 0:
      return 1
    return 0

  if a < 0 or b < 0 or c < 0:
    return 0

  if dp[total][a][b][c] != -1:
    return dp[total][a][b][c]

  dp[total][a][b][c] = 0
  for i in range(2):
    for j in range(2):
      for k in range(2):
        if i + j + k == 0:
          continue
        dp[total][a][b][c] += go(total - 1, a - i, b - j, c - k)
  dp[total][a][b][c] %= 1000000007
  return dp[total][a][b][c]

print(go(s, a, b, c))
