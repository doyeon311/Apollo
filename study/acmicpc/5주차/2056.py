# 2056
# 작업
import heapq

n = int(input())

times = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
in_degree = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
  row = list(map(int, input().split()))
  time = row[0]
  cnt = row[1]
  have_to = row[2:]
  in_degree[i] += cnt
  times[i] = time

  for work in have_to:
    graph[work].append(i)

q = []

temp = 0
for i in range(1, n + 1):
  if in_degree[i] == 0:
    heapq.heappush(q, (times[i], i))

answer = 0
while q:
  finish, now = heapq.heappop(q)
  # print(finish, now, f"({times[now]})", end=" -> ")
  answer = finish
  # print(in_degree)
  for next in graph[now]:
    in_degree[next] -= 1

    if in_degree[next] == 0:
      heapq.heappush(q, (finish + times[next], next))

print(answer)