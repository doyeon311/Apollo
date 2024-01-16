# 다익스트라 -> 특정 노드에서 다른 노드까지의 최단 시간
# c 도시에서 출발한 전보가 어디까지 퍼질 수 있는지
# 다 퍼지는데 걸릴 시간
import heapq

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

q = []
distance[c] = 0
heapq.heappush(q, (0, c))

while q:
  dist, now = heapq.heappop(q)

  if distance[now] < dist:
    continue

  for i in graph[now]:
    cost = dist + i[1]
    print(i, distance)
    if distance[i[0]] > cost:
      distance[i[0]] = cost
      heapq.heappush(q, (cost, i[0]))

reached = 0
time = 0

for d in distance:
  if d != INF and d != 0:
    reached += 1
    time = max(time, d)

print(reached, time)