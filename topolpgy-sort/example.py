# 위상 정렬 알고리즘
# O(V + E)
from collections import deque

v, e = map(int, input().split())
# v, e = [7,8]

# 모든 노드의 진입차수 0으로 초기화
indegree = [0] * (v + 1)
# 간선 연결 정보를 담기 위한 연결 리스트
graph = [[] for _ in range(v + 1)]
test = [
  [1,2],
  [1,5],
  [2,3],
  [2,6],
  [3,4],
  [4,7],
  [5,6],
  [6,4],
]
for i in range(e):
  a, b = map(int, input().split())
  # a, b = test[i]
  graph[a].append(b)
  indegree[b] += 1

def topology_sort():
  result = []
  q = deque()

  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
  
  for i in result:
    print(i, end=' ')

topology_sort()
