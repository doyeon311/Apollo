# 계수 정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(arr) + 1)

for a in arr:
  count[a] += 1
print(count)
for idx, cnt in enumerate(count):
  for i in range(cnt):
    print(idx, end=" ")