# 괄호

n = int(input())

ps_list = []

for _ in range(n):
  ps = input()
  ps_list.append(ps)

for ps in ps_list:
  flag = 0
  for p in ps:
    if p == '(':
      flag += 1
    elif p == ')':
      flag -= 1
    # print(flag)
    if flag < 0:
      print('NO')
      break
  else:
    if flag == 0:
      print('YES')
    else:
      print('NO')