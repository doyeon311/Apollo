# DFS와 BFS
n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

visited = [False] * (n + 1)

def dfs(i):
  visited[i] = True
  print(i, end=" ")
  for j in range(1, n + 1):
    if visited[j] == False and graph[i][j] == 1:
      dfs(j)

def bfs(v):
  visited = [False] * (n + 1)
  q = [v]
  visited[v] = True

  while q:
    current = q.pop(0)
    print(current, end=" ")
    for next in range(1, n + 1):
      if visited[next] == False and graph[current][next] == 1:
        q.append(next)
        visited[next] = True

dfs(v)
print()
bfs(v)