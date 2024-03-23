# 다익스트라 1
# O(V^2)

import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
# n, m = map(int, input().split())
n, m = [6, 11]

# 시작 노드
# start = int(input())
start = 1

# 노드 연결 정보
graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
distance = [INF] * (n + 1)

temp = [
  [1, 2, 2],
  [1, 3, 5],
  [1, 4, 1],
  [2, 3, 3],
  [2, 4, 2],
  [3, 2, 3],
  [3, 6, 5],
  [4, 3, 3],
  [4, 5, 1],
  [5, 3, 1],
  [5, 6, 2],
]

# for _ in range(m):
for t in temp:
  # a에서 b까지 가는 비용이 c
  # a, b, c = map(int, input().split())
  a, b, c = t
  graph[a].append((b, c))

def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n + 1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  
  # start에 연결된 노드에서 j[0]까지 가는 비용이 j[1]
  for j in graph[start]:
    distance[j[0]] = j[1]
  
  for _ in range(n - 1): # 시작 노드 제외
    now = get_smallest_node()
    visited[now] = True

    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])


# 복습 ============================================================
# n, m = map(int, input().split())
INF = int(1e9)

# start = int(input())
# graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# for _ in range(m):
#   a, b, c = map(int, input().split())

#   graph[a].append((b, c))

def get_smallest_node():
  index = -1

  for i in range(1, n + 1):
    if visited[i] == False and distance[i] < distance[index]:
      index = i
  return index

distance[start] = 0
visited[start] = 0

for d in graph[start]:
  distance[d[0]] = d[1]

for _ in range(n + 1):
  smallest = get_smallest_node()
  visited[smallest] = True

  for d in graph[smallest]:
    cost = distance[smallest] + d[1]
    if distance[d[0]] > cost:
      distance[d[0]] = cost

print(distance)