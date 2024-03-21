# 선택 정렬

arr = [7, 3, 2, 5, 1, 0, 4, 9, 8, 6]

for i in range(len(arr)):
  min_idx = i
  for j in range(i, len(arr)):

    if arr[j] < arr[min_idx]:
      min_idx = j

  arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)