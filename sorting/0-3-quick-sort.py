# 퀵 정렬

# 호어분할
arr = [7, 3, 2, 5, 1, 0, 4, 9, 8, 6]

def quick_sort(arr, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  print(arr)
  while right >= left:
    while left <= end and arr[left] <= arr[pivot]:
      left += 1
    while right > start and arr[right] >= arr[pivot]:
      right -= 1
    
    if left >= right:
      arr[right], arr[pivot] = arr[pivot], arr[right]
    else:
      arr[left], arr[right] = arr[right], arr[left]
    
  quick_sort(arr, start, right - 1)
  quick_sort(arr, right + 1, end)


quick_sort(arr, 0, len(arr) - 1)
print(arr)


# 파이썬
def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  
  pivot = arr[0]
  tail = arr[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)