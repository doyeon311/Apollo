# 2133
# 타일 채우기
n = int(input())
dp = [0] * (n + 2)
dp[0] = 1
dp[2] = 3
for i in range(4, n + 1, 2):
  dp[i] = dp[i-2] * 3 + sum(dp[:i-3:2]) * 2

print(dp[n])