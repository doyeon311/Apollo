# 왕실의 나이트

moves = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

cols = ' abcdefgh'

print(cols.index('a'))

position = input()

col = cols.index(position[0])
row = int(position[1])

cnt = 0
for move in moves:
  dc, dr = move
  next_col = col + dc
  next_row = row + dr

  if 1 <= next_row <= 8 and 1 <= next_col <= 8:
    cnt += 1

print(cnt)