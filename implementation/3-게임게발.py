# 게임 개발
# field: N x M
# sea or land

# 반시계 방향으로 회전
# 0: 북, 1: 동, 2: 남, 3: 서
directs = [[-1, 0], [0, -1], [1, 0], [0, 1]]

visits = 1

# n, m = map(int, input().split())
# a, b, d = map(int, input().split())
n, m = [4, 4]
a, b, d = [1, 1, 0]

current_position = (a, b)
current_direction = directs[d] # 왼쪽부터 탐색 시작

field = []
temp = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
# for _ in range(n):
for i in temp:
  # row = list(map(int, input().split()))
  row = i
  field.append(row)
  print(row)

print(current_direction, current_position)
field[current_position[0]][current_position[1]] = -1
# 현재 위치, 현재 방향에서 왼쪽부터 차례대로 돌아가면서 갈 수 있는 곳을 고름
# 

limit = 4

temp = 20
while temp > 0:
  print("==================")
  d = (d + 1) % 4
  dx, dy = directs[d] # 왼쪽부터 탐색
  x, y = current_position
  next_x = x + dx
  next_y = y + dy
  temp -= 1
  print(limit, ' / ', visits, current_position, [next_x, next_y])

  if field[next_x][next_y] == 0:
    visits += 1
    field[next_x][next_y] = -1
    print('땅', field[next_x][next_y])
    current_position = (next_x, next_y)
    limit = 4
    continue
  else:
    print('바다 or 가본 곳')
    limit -= 1

  if limit == 0:
    back_x = x - dx
    back_y = y - dy
    limit = 4
    
    if field[back_x][back_y] == 1:
      print('바다')
      break
    else:
      current_position = (back_x, back_y)

print(visits)
  