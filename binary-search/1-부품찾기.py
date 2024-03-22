# 부품찾기

# 이진탐색 ================================================================================

# n개 부품
# m 종류의 부품을 대량 주문
# m 가지 종류의 부품이 다 있는지 확인하는 프로그램

def binary_search(arr, target, start, end):
  if start > end:
    return None
  
  mid = (start + end) // 2

  if arr[mid] == target:
    return True
  elif arr[mid] > target:
    return binary_search(arr, target, start, mid - 1)
  else:
    return binary_search(arr, target, mid + 1, end)


n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
order_list = list(map(int, input().split()))

n_list.sort()

for order in order_list:
  result = binary_search(n_list, order, 0, n - 1)

  if result:
    print('yes', end=" ")
  else:
    print('no', end=" ")


# 계수 정렬 ================================================================================
board = [0] * 1000001

for n in n_list:
  board[n] += 1

for order in order_list:
  if board[order] > 0:
    print('yes', end=" ")
  else:
    print('no', end=" ")

# set ================================================================================
arr = set(n_list)

for order in order_list:
  if order in arr:
    print('yes', end=" ")
  else:
    print('no', end=" ")