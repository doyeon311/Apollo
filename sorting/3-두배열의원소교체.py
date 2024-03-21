# 두 배열의 원소 교체
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  for j in range(i, n):
    if a[j] < b[j]:
      a[j], b[j] = b[j], a[j]
    else:
      break
  
  print(a)
  print(b)
  print("=======")

print(a, b)
print(sum(a))