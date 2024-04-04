# 소수 구하기
# m 이상 n 이하의 소수를 모두 출력하는 프로그램

m, n = map(int, input().split())

board = [True] * (n + 1)

for i in range(2, (n // 2) + 1):
  if board[i] == False:
    continue
  for j in range(2, (n // i) + 1):
    if i * j <= n:
      board[i * j] = False
    else:
      break

for idx, b in enumerate(board[m:n+1]):
  num = idx + m
  if b and num != 1:
    print(idx + m)