# 수 정렬하기

n = int(input())

list = []
for _ in range(n):
  item = int(input())
  list.append(item)

list1 = list.copy()

for i in range(n):
  exchange = 0
  for j in range(n-1, i, -1):
    if list1[j-1] > list1[j]:
      list1[j-1], list1[j] = list1[j], list1[j-1]
      exchange += 1
  if exchange == 0:
    break

print(list1)

list2 = list.copy()

k = 0 # 이미 정렬된 요소는 제외하기 위해 할 범위를 표시 k ~ n-1

while k < n - 1:
  last = n - 1
  for j in range(n-1, k, -1):
    if list1[j-1] > list1[j]:
      list1[j-1], list1[j] = list1[j], list1[j-1]
      last = j
  k = last
print(list1)




# for _ in range(n):
#   item = int(input())
#   list.append(item)

# list.sort()

for item in list:
  print(item)




