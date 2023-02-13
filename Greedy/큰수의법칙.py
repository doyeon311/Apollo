# 큰 수의 법칙 - 이코테

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 데이터 큰 순서대로 정렬
data.sort()
# 가장 큰 수롤 구하는 방법은
# data에서 가장 큰 수 / 두번째로 큰 수를 k번씩 번갈아 더하는 방법
first = data[n-1]
second = data[n-2]
print(first, second, data)
result = 0

# 총 M번 힌 번에 최대 K번
# first K번
# M = 8 K = 3
# 1 2 3 4 5 6 7 8
# f f f s f f f s

# 1
standard = m // (k + 1)

result += first * standard * k + second * standard

# 2
# while True:
#   for i in range(k):
#     if m == 0:
#       break
#     result += first
#     m -= 1
  
#   if m == 0:
#     break
#   result += second
#   m -= 1


print(result)
