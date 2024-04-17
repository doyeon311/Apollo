# 1062
# 가르침
n, k = map(int, input().split())

if k < 5:
  print(0)
  exit()
elif k == 26:
  print(n)
  exit()

result = 0

required = ['a', 'n', 't', 'i', 'c'] # 5
optional = []
words = []

learned = [0] * 26

for _ in range(n):
  word = list(set(list(input())[4:-4]))
  words.append(word)

for c in required:
  learned[ord(c) - ord('a')] = 1

def dfs(idx, cnt):
  global result

  if cnt == k - 5:
    read_cnt = 0
    for word in words:
      flag = True
      for w in word:
        if not learned[ord(w) - ord('a')]:
          flag = False
          break
      if flag:
        read_cnt += 1
    result = max(result, read_cnt)
    return
  
  for i in range(idx, 26):
    if not learned[i]:
      learned[i] = 1
      dfs(i, cnt + 1)
      learned[i] = 0

dfs(0, 0)
print(result)
