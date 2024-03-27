# 골드바흐의 추측
# 4보다 큰 모든 짝수는 홀수 소수의 합으로 나타낼 수 있다.
import sys

def input():
  return sys.stdin.readline()

MAX_NUM = 1000000

board = [True] * (MAX_NUM + 1)

board[0] = False
board[1] = False

for i in range(2, int(MAX_NUM ** 0.5) + 1):
  if board[i] == False:
    continue
  for j in range(i + i, MAX_NUM, i):
    board[j] = False


# print(board)

while True:
  num = int(input())
  flag = True
  if num == 0:
    break

  # board를 돌면서 board[idx] board[num - idx] 모두 True인지 확인
  # print(num // 2)
  for i in range(3, (num // 2) + 1, 2):
    # print(i, num - i, board[i], board[num -i])
    if board[i] and board[num - i]:
      print(f'{num} = {i} + {num - i}')
      flag = False
      break
  
  if flag:
    print("Goldbach's conjecture is wrong.")
  




