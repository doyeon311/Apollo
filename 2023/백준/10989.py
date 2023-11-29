# 수 정렬하기 3
# 오름차순으로 정렬
import sys

# list 길이 입력
n = int(sys.stdin.readline())

# list 입력 1 ~ 10000
# counting sort 계수정렬
list = [0] * 10001
for _ in range(n):
  num = int(sys.stdin.readline())
  list[num] += 1

for num, count in enumerate(list):
  if num != 0:
    for _ in range(count):
      print(num)


# list 입력 1 ~ 10000
# list = []
# for _ in range(n):
#   list.append(int(sys.stdin.readline()))

# 쉐이커 정렬
# left = 0
# right = n - 1
# last = n - 1

# while left < right:
#   for j in range(right, left, -1):
#     if list[j-1] > list[j]:
#       list[j-1], list[j] = list[j], list[j-1]
#       last = j
#   left = last

#   for j in range(left, right):
#     if list[j] > list[j+1]:
#       list[j], list[j+1] = list[j+1], list[j]
#       last = j
#   right = last

# print(list)

for num in list:
  print(num)
