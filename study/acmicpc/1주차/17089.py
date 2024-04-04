# 세 친구

MAX_NUM = 987654321

n, m = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())

  graph[a][b] = graph[b][a] = True

def count_friends(selected_list):
  result = 0
  for i in range(3):
    person = selected_list[i]
    for friend, is_friend in enumerate(graph[person]):
      if is_friend and friend not in selected_list:
        result += 1

  return result

def is_friend(selected_list, a):
  for person in selected_list:
    if graph[a][person] == False:
      return False
  return True

# 사람 n 중에 3명을 고름
selected = [False] * (n + 1)
def select(current, selected, selected_list):
  if len(selected_list) == 3:
    return count_friends(selected_list)
  
  result = MAX_NUM

  for i in range(current, n + 1):
    if selected[i] == False and is_friend(selected_list, i):
      selected[i] = True
      friends = select(i + 1, selected, selected_list + [i])
      result = min(friends, result)
      selected[i] = False
  return result

result = select(1, selected, [])

if result == MAX_NUM:
  print(-1)
else:
  print(result)