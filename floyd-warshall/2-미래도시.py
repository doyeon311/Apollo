# 미래도시
# n, m = map(int, input().split())
n, m = [5, 7]

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]
temp = [
  [1, 2],
  [1, 3],
  [1, 4],
  [2, 4],
  [3, 4],
  [3, 5],
  [4, 5],
]
# for _ in range(m):
#   a, b = map(int, input().split())
for a, b in temp:
  graph[a][b] = 1
  graph[b][a] = 1

for i in range(1, n + 1):
  graph[i][i] = 0

# x, k = map(int, input().split())
x, k =[4, 5]

# 1 -> K
# K -> X

for g in graph:
  print(g)
print("======================================================")
for m in range(1, n + 1):
  for start in range(1, n + 1):
    for end in range(1, n + 1):
      print(start, "=>", end,'=', graph[start][end], 'vs', graph[start][m] + graph[m][end])
      graph[start][end] = min(graph[start][end], graph[start][m] + graph[m][end])

for g in graph:
  print(g)

print(graph[1][k] + graph[k][x])