# 11052
# 카드 구매하기

n = int(input())
p = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = p[1]
# dp[2] = p[2] or dp[1] + p[1]
# dp[3] = p[3] or dp[2] + p[1] or dp[1] + p[2]

# N개를 구매하기 위해 지불해야하는 최대가격

for current in range(2, n + 1):
  dp[current] = p[current]
  for i in range(1, current + 1):
    dp[current] = max(dp[current], dp[i] + p[current - i])

print(dp[n])

