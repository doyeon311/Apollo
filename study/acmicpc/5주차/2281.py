# 2281
# 데스노트
n, m = map(int, input().split())
names = []
for _ in range(n):
  names.append(int(input()))

maxValue = m*m*n

dp = [maxValue for _ in range(n + 1)]
dp[n] = 0
def dfs(index):
  if dp[index] < maxValue:
    return dp[index]
  
  remain = m - names[index]
  for i in range(index + 1, n + 1):
    if remain >= 0:
      if i == n:
        dp[index] = 0
        break
      dp[index] = min(dp[index], remain*remain + dfs(i))
      remain -= names[i] + 1
  return dp[index]

print(dfs(0))




