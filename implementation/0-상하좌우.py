# 상하좌우
# NxN

position = [1, 1]
direction = {
  "L": [0, -1],
  "R": [0, 1],
  "U": [-1, 0],
  "D": [1, 0],
}

n = int(input())
route = list(input().split())

for r in route:
  print('now', position, 'direction', direction[r])
  next_x = position[0] + direction[r][0]
  next_y = position[1] + direction[r][1]

  if next_x < 1 or next_x > n or next_y < 1 or next_y > n:
    continue

  position = [next_x, next_y]

print(position)