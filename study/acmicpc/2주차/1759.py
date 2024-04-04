# 암호 만들기

# 서로 다른 L개의 알파벳 소문자로 된 암호

# 최소 한 개의 모음 a e i o u
# 최소 두 개의 자음
# 알파벳이 증가하는 순서로 배열

# C 개의 문자가 주어짐
# 가능성 있는 암호를 모두 구하라

l, c = map(int, input().split())

alpha = input().split()
alpha.sort()

# consonant 에서 최소 1개
# vowel 에서 최소 2개

def is_available(password):
  c_cnt = 0
  v_cnt = 0
  for p in password:
    if p in ['a', 'e', 'i', 'o', 'u']:
      c_cnt += 1
    else:
      v_cnt += 1
  return c_cnt >= 1 and v_cnt >= 2

def dfs(current_str, current_idx):
  if len(current_str) == l:
    if is_available(current_str):
      print(current_str)
    return

  for a in range(current_idx, c):
    dfs(current_str + alpha[a], a + 1)

dfs('', 0)
