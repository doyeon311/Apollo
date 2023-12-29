# 평범한 배낭
import math

n, k = map(int, input().split())

weights = []
values = []
for i in range(n):
  w, v = map(int, input().split())

  weights.append(w)
  values.append(v)


dp = [[0] * (k+1) for _ in range(n+1)]


for i in range(1, n+1):
  for w in range(1, k+1):
    if (weights[i-1] <= w):
      dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i - 1][w])
    else:
      dp[i][w] = dp[i-1][w]
# print(values)
# print(values)
# print(dp)
# for d in dp:
#   print(d)
print(dp[n][k])