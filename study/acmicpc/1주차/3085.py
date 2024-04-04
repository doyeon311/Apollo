# 사탕 게임
# 색이 다른 인접한 사탕 두개의 자리를 바꿈
# 연속된 사탕 중 제일 긴

n = int(input())

candies = []

for _ in range(n):
  candies.append(list(input()))


# exchange candy
# 인접하고 서로 다른 캔디를 교환
# 인접
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0] 

# get rows
def get_max_row(candies):
  h_max_cnt = 0
  v_max_cnt = 0

  for i in range(n):
    h_temp = ""
    h_cnt = 1
    v_temp = ""
    v_cnt = 1
    for j in range(n):
      if h_temp == candies[i][j]:
        h_cnt += 1
        h_max_cnt = max(h_cnt, h_max_cnt)
      else:
        h_temp = candies[i][j]
        h_cnt = 1

      if v_temp == candies[j][i]:
        v_cnt += 1
        v_max_cnt = max(v_cnt, v_max_cnt)
      else:
        v_temp = candies[j][i]
        v_cnt = 1

  return max(v_max_cnt, h_max_cnt)


result = 0
for x in range(n):
  for y in range(n):
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if 0 <= nx < n and 0 <= ny < n and candies[x][y] != candies[nx][ny]:
        candies[x][y], candies[nx][ny] = candies[nx][ny], candies[x][y]
        max_row = get_max_row(candies)
        result = max(max_row, result)
        candies[x][y], candies[nx][ny] = candies[nx][ny], candies[x][y]

print(result)
