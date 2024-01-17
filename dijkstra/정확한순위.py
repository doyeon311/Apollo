# 정확한 순위
# 정확한 순위를 알 수 있는 학생의 수

# n, m = map(int, input().split())
n, m = [6, 6]
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  graph[i][i] = 0

test = [
  [1,5],
  [3,4],
  [4,2],
  [4,6],
  [5,2],
  [5,4],
]

for i in range(m):
  # a, b = map(int, input().split())
  a, b = test[i]
  graph[a][b] = 1

for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n + 1):
  count = 0
  for j in range(1, n + 1):
    if graph[i][j] != INF or graph[j][i] != INF:
      count += 1
  if count == n:
    result += 1

print(result)

    