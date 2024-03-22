# 떡볶이 떡 만들기

# 서로 다른 길이의 떡볶이 떡
# 절단기로 한번에 잘랐을 때 손님이 요청한 길이 M을 만족하는 최대 높이는?

# n, m = map(int, input().split())
# cakes = list(map(int, input().split()))

n, m = [4, 6]
cakes = [19, 15, 10, 17]

def binary_search(arr, target, start, end):
  result = 0
  while start <= end:
    mid = (start + end) // 2
    
    total = 0

    for a in arr:
      if a > mid:
        total += (a - mid)

    print(target, "-----", mid, total)

    if total == target:
      return mid
    elif total > target:
      result = mid
      start = mid + 1
    else:
      end = mid - 1

  return result

print(binary_search(cakes, m, 0, max(cakes)))
