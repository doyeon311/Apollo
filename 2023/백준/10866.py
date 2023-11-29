# 덷
import sys

def input():
  return sys.stdin.readline()

n = int(input())
list = []

for _ in range(n):
  command = input().split()

  if command[0] == 'push_front':
    list = [command[1]] + list
  elif command[0] == 'push_back':
    list.append(command[1])
  elif command[0] == 'pop_front':
    if len(list) == 0:
      print(-1)
    else:
      print(list[0])
      list = list[1:]
  elif command[0] == 'pop_back':
    if len(list) == 0:
      print(-1)
    else:
      print(list.pop())
  elif command[0] == 'size':
    print(len(list))
  elif command[0] == 'empty':
    print(1 if len(list) == 0 else 0)
  elif command[0] == 'front':
    if len(list) == 0:
      print(-1)
    else:
      print(list[0])
  elif command[0] == 'back':
    if len(list) == 0:
      print(-1)
    else:
      print(list[-1])
  # print(list)