# 숫자카드게임

n, m = map(int, input().split())

result = 0

for _ in range(n):
  nums = list(map(int, input().split()))
  result = max(result, min(nums))

print(result)