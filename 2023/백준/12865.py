# 평범한 배낭

# n 물건 개수
# k 제한 무게
n, k = map(int, input().split())

weights = []
values = []
for i in range(n):
  w, v = map(int, input().split())
  weights.append(w)
  values.append(v)

# x: 제한 무게별
# y: 물건 개수별
dp = [[0] * (k+1) for _ in range(n+1)]

# 물건 개수 1 ~ n
for i in range(1, n+1):
  # 무게 1 ~ k
  for w in range(1, k+1):
    # 물건 i개 제한 무게 w일 때
    if (weights[i-1] <= w):
      # i의 가치 + 같은 개수를 넣는 경우 중에 w-weight[i-1]를 더했을 때의 가치, i-1개를 w무게 만큼 넣는 경우 중 큰 가치를 저장
      dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i - 1][w])
    else:
      # 더이상 넣을 수 없는 경우엔 직전에 계산해둔 가치로 저장
      dp[i][w] = dp[i-1][w]
# print(values)
# print(values)
# print(dp)
# for d in dp:
#   print(d)
print(dp[n][k])