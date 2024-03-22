# 효율적인 화폐구성

n, m = map(int, input().split())

money = []
for _ in range(n):
  money.append(int(input()))

dp = [10001] * 10001

for num in money:
  dp[num] = 1

for i in range(0, m + 1):
  print('i = ',i)
  for num in money:
    if i - num > 0:
      print(i - num)
      dp[i] = min(dp[i], dp[i-num] + 1)
  print("====")

print(m, dp[m])


d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
  for j in range(money[i], m + 1):
    if d[j - money[i]] != 10001:
      d[j] = min(d[j], d[j - money[i]])