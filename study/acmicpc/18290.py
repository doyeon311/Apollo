# NM과 K(1)
# N X M 크기의 격자판
# 이 중에서 K개 선택
# 선택된 수는 인접하면 안됨

n, m, k = map(int, input().split())
selected = [[False] * m for _ in range(n)]
board = []

for _ in range(n):
  board.append(list(map(int, input().split())))
# print(board)

def is_selectable(x, y, selected):
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    # nx, ny가 board의 범위 내이고
    if 0 <= nx < n and 0 <= ny < m:
      # 이미 선택된 수가 주변에 있으면 선택 불가능
      if selected[nx][ny]:
        return False
  # 주변에 이미 선택된 수가 없으면 선택 가능
  return True

def back_tracking(x, selected, selected_nums, cnt):
  if len(selected_nums) == k:
    # print(selected_nums, sum(selected_nums))
    return sum(selected_nums)
  
  result = -987654321
  for i in range(x, n):
    for j in range(m):
      # 선택된 적이 없고, 주변에도 선택된 수가 없으면
      if selected[i][j] == False and is_selectable(i, j, selected):
        selected[i][j] = True
        sum_selected_num = back_tracking(i, selected, selected_nums + [board[i][j]], cnt+1)
        result = max(result, sum_selected_num)
        selected[i][j] = False
  
  return result

print(back_tracking(0, selected, [], 0))