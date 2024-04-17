# 10819
# 차이를 최대로

n = int(input())
nums = list(map(int, input().split()))
selected = [False] * n

def calculate(num_list):
  score = 0

  for i in range(n - 1):
    score += abs(num_list[i] - num_list[i + 1])
  return score

max_score = 0

def dfs(num_list):
  global max_score

  if len(num_list) == n:
    score = calculate(num_list)
    max_score = max(score, max_score)
    return
  
  for i in range(n):
    if selected[i] == False:
      selected[i] = True
      dfs(num_list + [nums[i]])
      selected[i] = False

dfs([])

print(max_score)