def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  
  return None


n, target = map(int, input().split())

arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n - 1)
if result == None:
  print('없습니다')
else:
  print(result + 1)