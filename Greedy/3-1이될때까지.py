# 1이 될 때까지

n, k = map(int, input().split())

cnt = 0

while n > 1:
  print(n)
  if n % k == 0:
    cnt += 1
    n = n // k
  else:
    cnt += 1
    n -= 1
print("-----",n)
print(cnt)