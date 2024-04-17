# 10972
# 다음 순열
n = int(input())
num = list(map(int, input().split()))

def next_permutation(num, n):
  i = n - 1

  while i > 0 and num[i - 1] > num[i]:
    i -= 1

  if i <= 0:
    return False
  
  j = n - 1

  while num[j] <= num[i-1]:
    j -= 1
  
  num[i-1], num[j] = num[j], num[i-1]

  j = n - 1

  while i < j:
    num[i], num[j] = num[j], num[i]
    i += 1
    j -= 1
  return True

next_num = next_permutation(num, n)

if next_num:
  print(' '.join(list(map(str, num))))
else:
  print(-1)
