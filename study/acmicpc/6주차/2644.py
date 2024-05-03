# 2644
# 촌수계산


n = int(input())
a, b = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n + 1)]

visited = [0] * (n + 1)

for _ in range(m):
  x, y = map(int, input().split())

  graph[x].append(y)
  graph[y].append(x)

q = [a]

while q:
  current = q.pop(0)

  if current == b:
    break

  for next in graph[current]:
    if visited[next] == 0:
      q.append(next)
      visited[next] += visited[current] + 1

if visited[b] == 0:
  print(-1)
else:
  print(visited[b])