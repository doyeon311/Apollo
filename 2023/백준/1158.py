# 요세푸스 문제

n, k = map(int, input().split())
# n, k = [7, 3]

nums = [num for num in range(1, n+1)]

# n번 삭제
target = 0
print('<', end='')
for i in range(n):
  target = (target + k - 1) % len(nums)
  print(nums[target], end='')
  nums.pop(target)
  if i != n-1:
    print(', ', end='')
print('>', end='')



# print('<', end='')
# print(', '.join(list(map(str, result))), end='')
# print('>', end='')
