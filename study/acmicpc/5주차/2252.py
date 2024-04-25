# 2252
# 줄 세우기

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  degree[b] += 1

q = []
answer = []

for i in range(1, n + 1):
  if degree[i] == 0:
    q.append(i)

while q:
  current = q.pop(0)
  answer.append(current)

  for i in graph[current]:
    degree[i] -= 1

    if degree[i] == 0:
      q.append(i)

print(*answer)

