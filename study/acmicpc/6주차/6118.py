# 6118
# 숨바꼭질
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())

  graph[a].append(b)
  graph[b].append(a)

q = [1]

while q:
  current = q.pop(0)

  for next in graph[current]:
    if visited[next] == 0 and next != 1:
      q.append(next)
      visited[next] += visited[current] + 1

hide = 0
distance = max(visited)
hide_cnt = 0

for idx in range(n, 0, -1):
  if visited[idx] == distance:
    hide = idx
    hide_cnt += 1

print(hide, distance, hide_cnt)
