# 퇴사
# N + 1 날 퇴사
# 남은 날 N

# 상담하는데 걸리는 기간 T[i]
# 받을 수 있는 금액 P[i]

n = int(input())

dp = [0] * (n + 1)

T = [] # 상담하는데 걸리는 기간
P = [] # 받을 수 있는 금액

for _ in range(n):
  t, p = map(int, input().split())
  T.append(t)
  P.append(p)

for i in range(n):
  current_t = T[i]
  current_p = P[i]

  if i + current_t < n + 1:
    dp[i + current_t] = max(max(dp[:i + 1]) + current_p, dp[i + current_t])

print(max(dp))

# 1, 2, 3, 4
# 3, 5, 1, 1
# 10 20 10 20
# [0, 0, , 10, 30, 0, 20]