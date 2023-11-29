# 수 정렬하기 2
import sys
import heapq

n = int(sys.stdin.readline())
list = []

for _ in range(n):
  num = int(sys.stdin.readline())
  list.append(num)

# print("list", list)

# 빌트인 함수 ======================================
# list.sort()

# 쉐이커 정렬 ======================================
# left = 0
# right = n - 1
# last = right

# while left < right:
#   # print('left <= right', left, right)
#   for j in range(right, left, -1):
#     if list[j-1] > list[j]:
#       list[j-1], list[j] = list[j], list[j-1]
#       last = j
#       # print(j, last, list)
#   left = last
  
#   # print('left => right', left, right)
#   for j in range(left, right):
#     if list[j] > list[j+1]:
#       list[j], list[j+1] = list[j+1], list[j]
#       last = j
#       # print(list)
#   right = last


# for i in list:
#   print(i)

# 힙소팅 ======================================
heap = []
for i in list:
  heapq.heappush(heap, i)

for i in range(n):
  print(heapq.heappop(heap))

