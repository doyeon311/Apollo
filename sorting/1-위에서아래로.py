# 위에서 아래로
# 내림차순으로 정렬
# 1 <= n <= 500
n = int(input())

arr = []
for _ in range(n):
  arr.append(int(input()))

arr.sort(reverse=True)

print(arr)