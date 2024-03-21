# 삽입 정렬
# 2번째부터 시작하여 앞 값들과 비교하여 들어갈 자리를 찾음

arr = [7, 3, 2, 5, 1, 0, 4, 9, 8, 6]

for i in range(1, len(arr)):
  for j in range(i, 0, -1):
    if arr[j] < arr[j-1]:
      arr[j], arr[j-1] = arr[j-1], arr[j]
    else:
      break

print(arr)