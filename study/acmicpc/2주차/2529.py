# 부등호

# bfs?

# k 길이의 부등호
# k + 1 길이의 수
# 주어진 부등호들을 만족하는 수
# 만족하는 수 중 최댓값과 최소값

k = int(input())

signs = input().split()

selected = [False] * 10

mx, mn = "", ""

def dfs(num_str):
  global mx, mn
  if len(num_str) == k + 1:
    if mn == "":
      mn = num_str
    else:
      mx = num_str
    return

  sign = signs[len(num_str) - 1]
  # 큰 수를 찾아야 하면
  if sign == '<':
    for i in range(int(num_str[-1]), 10):
      if selected[i] == False:
        selected[i] = True
        dfs(num_str + str(i))
        selected[i] = False
  elif sign == '>':
    for i in range(int(num_str[-1])):
      if selected[i] == False:
        selected[i] = True
        dfs(num_str + str(i))
        selected[i] = False



for i in range(10):
  selected[i] = True
  dfs(str(i))
  selected[i] = False

print(mx)
print(mn)