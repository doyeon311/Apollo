# 다익스트라 1
# O(V^2)

import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())

# 시작 노드
start = int(input())

# 노드 연결 정보
graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
  # a에서 b까지 가는 비용이 c
  a, b, c = map(int, input().split())
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
