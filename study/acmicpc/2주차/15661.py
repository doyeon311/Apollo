# 링크와 스타트

# 총 N 명의 사람들
# 두 팀으로 나눠서 - 팀의 인원은 같지 않아도 됨 하지만 1명 이상이어야함

# S[i][j] i와 j가 같은 팀에 속했을 때 팀에 더해지는 능력치
# S[i][j] S[j][i]는 다를 수 있음

# 두 팀의 능력치 차이를 최소로

n = int(input())

S = []

for _ in range(n):
  row = list(map(int, input().split()))
  S.append(row)

visited = [False] * n

def check_score():
  start_score = 0
  link_score = 0
  for i in range(n):
    for j in range(n):
      if visited[i] and visited[j]:
        start_score += S[i][j]
      elif not visited[i] and not visited[j]:
        link_score += S[i][j]
      
  return abs(start_score - link_score)

result = int(1e9)

def dfs(start, current):
  global result
  start_cnt = len(start)
  if start_cnt > 0:
    result = min(result, check_score())
  
  if start_cnt == n:
    return
  
  for i in range(current, n):
    visited[i] = True
    dfs(start + [i], i + 1)
    visited[i] = False

dfs([], 0)

print(result)