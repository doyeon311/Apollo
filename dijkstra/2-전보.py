# 전보
import heapq

INF = int(1e9)
# n, m, c= map(int, input().split())
n, m, c = [3, 2, 1]

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

temp = [
  [1, 2, 4],
  [1, 3, 2]
]

# for _ in range(m + 1):
#   x, y, z = map(int, input().split())
for x, y, z in temp:
  graph[x].append((y, z))

q = []
heapq.heappush(q, (0, c))
distance[c] = 0

while q:
  dist, now = heapq.heappop(q)

  if dist > distance[now]:
    continue

  for g in graph[now]:
    cost = dist + g[1]

    if cost < distance[g[0]]:
      distance[g[0]] = cost
      heapq.heappush(q, (cost, g[0]))

cnt = 0
max_time = 0
print(INF == 1000000000)
for dist in distance:
  print(dist, dist != INF)
  if dist != INF:
    cnt += 1
    max_time = max(max_time, dist)
print(distance, cnt - 1, max_time)