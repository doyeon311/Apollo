# 단어 정렬

n = int(input())

words = set([])
for _ in range(n):
  word = input()
  words.add(word)

words_list = list(words)

words_list.sort()
words_list.sort(key=len)

for word in words_list:
  print(word)