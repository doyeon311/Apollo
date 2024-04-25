# 13023
# ABCDE

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


visited = [False] * n
result = 0
def dfs(cnt, current):
  global result
  if cnt == 0:
    result = 1
    return
  
  for i in graph[current]:
    if visited[i] == False:
      visited[i] = True
      dfs(cnt - 1, i)
      visited[i] = False


for i in range(n):
  visited[i] = True
  dfs(4, i)
  visited[i] = False
  if result == 1:
    break

print(result)


