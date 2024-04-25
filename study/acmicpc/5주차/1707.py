# 1707
# 이분 그래프
import sys
def input():
  return sys.stdin.readline()

def bfs(start, group):
  result = 'YES'
  q = [start]
  visited[start] = group
  while q:
    current = q.pop(0)

    for next in graph[current]:
      if visited[next] == False:
        q.append(next)
        visited[next] = -1 * visited[current]
      elif visited[next] == visited[current]:
        return False
  return True

k = int(input())

for _ in range(k):
  v, e = map(int, input().split())
  # v 정점의 개수
  # e 간선의 개수
  graph = [[] for _ in range(v + 1)]

  for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  
  visited = [False] * (v + 1)
  for i in range(1, v + 1):
    if visited[i] == False:
      result = bfs(i, 1)
    if result == False:
      break

  print("YES" if result else "NO")