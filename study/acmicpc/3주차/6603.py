# 6603
# 로또

def combination(nums, n, combi, k):
  if n == k:
    if len(combi) == 6:
      print(' '.join(list(map(str, combi))))
    return
  
  combination(nums, n + 1, combi + [nums[n]], k)
  combination(nums, n + 1, combi, k)

while True:
  test_case = list(map(int, input().split()))
  if test_case[0] == 0:
    break

  k = test_case[0]
  nums = test_case[1:]

  combination(nums, 0, [], k)
  print()
