# 스택

# 정수를 저장하는 스택을 구현

# 입력으로 주어지는 명령을 처리
# push X
# pop
# size
# empty
# top
import sys

def stack(list, command, target = None):
  if command == 'push':
    list.append(target)
  elif command == 'pop':
    if len(list) == 0:
      print(-1)
    else:
      item = list.pop()
      print(item)
  elif command == 'size':
    print(len(list))
  elif command == 'empty':
    print(1 if len(list) == 0 else 0)
  elif command == 'top':
    if len(list) == 0:
      print(-1)
    else:
      print(list[-1])

# 명령의 수
n = int(sys.stdin.readline())
list = []

for _ in range(n):
  command = sys.stdin.readline().split()
  if len(command) == 1:
    stack(list, command[0])
  else:
    stack(list, command[0], int(command[1]))

