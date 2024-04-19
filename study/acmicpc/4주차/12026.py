# BOJ 거리

n = int(input())
blocks = list(input())

dp = [1000*1000] * n
dp[0] = 0

for i in range(n):
  current_block = blocks[i]
  for j in range(i, n):
    if (current_block == 'B' and blocks[j] == 'O') or (current_block == 'O' and blocks[j] == 'J') or (current_block == 'J' and blocks[j] == 'B'):
      dp[j] = min(dp[j], dp[i] + (j - i) * (j - i))

# print(dp)

if dp[n-1] == 1000000:
  print(-1)
else:
  print(dp[n-1])
