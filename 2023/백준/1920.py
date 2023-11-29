# 수 찾기

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# 찾은 수 m_list
# 있는지 확인할 n_list

def bin_search(n_list: list, key: int):
  count = 0
  pl = 0 # 맨 앞 인덱스
  pr = len(n_list) - 1 # 맨 끝 인덱스

  while True:
    pc = (pl + pr) // 2 # 증긴 인덱스
    if n_list[pc] == key:
      return pc
    elif n_list[pc] > key:
      pr = pc - 1
    else:
      pl = pc + 1

    if pl > pr:
      break

  return -1

n_list.sort()

for x in m_list:
  result = bin_search(n_list, x)
  if result == -1:
    print(0)
  else:
    print(1)

