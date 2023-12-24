# 스택 수열

# n = 8
# 43687521
# 12345678
# 125
# ++++--++-++-----
# 43687521

n = int(input())
# n = 8
# n = 5

goal = []
# goal = [4, 3, 6, 8, 7, 5, 2, 1]
# goal = [1, 2, 5, 3, 4]

for _ in range(n):
  num = int(input())
  goal.append(num)


goal_idx = 0

stack = []
result = []

for i in range(1, n+1):
  stack.append(i)
  result.append('+')

  while len(stack) > 0 and stack[len(stack)-1] == goal[goal_idx]:
    stack.pop()
    result.append('-')
    goal_idx += 1

if len(stack) == 0:
  for r in result:
    print(r)
else:
  print('NO')
