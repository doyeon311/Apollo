# 날짜 계산

# 1 <= E <= 15
# 1 <= S <= 28
# 1 <= M <= 19

e, s, m = map(int, input().split())
E = 15
S = 28
M = 19

cnt = 0
temp = 0
while temp <= E * S * M:
  temp = cnt * E + e

  if temp % S == s % S and temp % M == m % M:
    print(temp)
    break
  cnt += 1