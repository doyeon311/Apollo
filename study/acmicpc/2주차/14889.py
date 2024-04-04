# 스타트와 링크

# 모인 N명 짝수
# 반반 나눠서 스타트팀과 링크팀으로 경기
# S[i][j] -> i와 j가 같은 팀일 때의 능력치
# S[j][i] 와 S[i][j]는 다를 수 있음

# 스타트와 링크의 능력치 차이를 최소로
# 능력치 차이의 최소값

n = int(input())

s = []

for _ in range(n):
  row = list(map(int, input().split()))
  s.append(row)


# 한팀당 최대 10명
visited = [False] * n

def check_score(visited):
  team1 = 0
  team2 = 0

  for i in range(n):
    for j in range(n):
      if visited[i] and visited[j]:
        team1 += s[i][j]
      elif visited[i] == False and visited[j] == False:
        team2 += s[i][j]
  return abs(team1 - team2)

result = 100 * n

def dfs(visited_cnt, current, visited):
  global result

  if visited_cnt == n // 2:
    result = min(result, check_score(visited))
    return
  
  for i in range(current, n):
    if visited[i] == False:
      visited[i] = True
      dfs(visited_cnt + 1, i + 1, visited)
      visited[i] = False

dfs(0, 0, visited)
print(result)
