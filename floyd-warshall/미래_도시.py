# 플로이드 워셜

# 노드 n개
# 시작은 1
# 양방향
# 모든 비용은 1
# k를 경유
# 1 -> k + k -> x

import sys

input = sys.stdin.readline
INF = int(1e9)

# n, m = map(int, input().split())
# n, m = [5, 7]

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  graph[i][i] = 0

# test = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [4, 5]]
for i in range(m):
  a, b = map(int, input().split())
  # a, b = test[i]
  # 양방향
  graph[a][b] = 1
  graph[b][a] = 1


# x, k = map(int, input().split())
x, k = [4, 5]

# k를 거쳐 x로
# 1 -> k + k -> x
# 플로이드 워셜
for mid in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][mid] + graph[mid][b])

for g in graph:
  print(g)

answer = graph[1][k] + graph[k][x]

if answer >= INF:
  print(-1)
else:
  print(answer)