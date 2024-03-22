# 1로 만들기

x = int(input())

max_num = 30

dp = [max_num] * (max_num + 1)
dp[0] = 0
dp[1] = 0
for i in range(max_num + 1):

  if i + 1 <= max_num:
    dp[i+1] = min(dp[i+1], dp[i] + 1)
  if i * 2 <= max_num:
    dp[i*2] = min(dp[i*2], dp[i] + 1)
  if i * 3 <= max_num:
    dp[i*3] = min(dp[i*3], dp[i] + 1)
  if i * 5 <= max_num:
    dp[i*5] = min(dp[i*5], dp[i] + 1)
print(dp[x])
print(dp)

# ================================================

d = [0] * max_num

for i in range(2, x + 1):
  d[i] = d[i - 1] + 1

  if i % 2 == 0:
    d[i] = min(d[i // 2] + 1, d[i])
  if i % 3 == 0:
    d[i] = min(d[i // 3] + 1, d[i])
  if i % 5 == 0:
    d[i] = min(d[i // 5] + 1, d[i])

print(d)
print(d[x])

