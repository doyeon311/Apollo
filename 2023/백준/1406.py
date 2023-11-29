# 에디터
import sys

def input():
  return sys.stdin.readline().strip()

# L -> cursor - 1 맨 앞이면 무시
# D -> cursor + 1 맨 뒤면 무시
# B -> cursor 왼쪽을 삭제 맨 앞이면 무시
# P $ -> $를 왼쪽에 추가함

text = input()
# cursor = len(text)

n = int(input())

# for _ in range(n):
#   command = input().split()

#   if command[0] == 'L':
#     if cursor != 0:
#       cursor -= 1
#   elif command[0] == 'D':
#     if cursor != len(text):
#       cursor += 1
#   elif command[0] == 'B':
#     text = text[:cursor-1] + text[cursor:]
#     cursor -= 1
#   elif command[0] == 'P':
#     text = text[:cursor+1] + command[1] + text[cursor+1:]
#     cursor += 1
  # print(f"'{text[:cursor]}' ^ {text[cursor:]}")


left = list(text)
right = []

for _ in range(n):
  command = input().split()

  if command[0] == 'L':
    if len(left) != 0:
      item = left.pop()
      right.append(item)
  elif command[0] == 'D':
    if len(right) != 0:
      item = right.pop()
      left.append(item)
  elif command[0] == 'B':
    if len(left) != 0:
      left.pop()
  elif command[0] == 'P':
    left.append(command[1])
  # print(left, right)

print(''.join(left + list(reversed(right))))
