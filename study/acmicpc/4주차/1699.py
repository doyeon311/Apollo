# 제곱수의 합

n = int(input())

dp = [i for i in range(n + 1)]

for i in range(n // 2 + 1):
  if i * i > n:
    break

  dp[i*i] = 1

for i in range(1, n + 1):
  for j in range(1, n // 2 + 1):
    if i + j * j > n:
      break
    dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)

print(dp[n])
