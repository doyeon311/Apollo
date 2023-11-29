# 숫자 카드
# n개 숫자카드 (정수)
# 정수 m개

# n개의 숫자 카드 중에 m개의 숫자가 있는지 없는지

# 1 <= n <= 500000
# 정수는 -10000000 <= 정수 <= 10000000

# 1 <= m <= 500000
# 정수는 -10000000 <= 정수 <= 10000000

import sys

n = int(input())
card_list = list(map(int, input().split()))
# print(n, card_list)

m = int(input())
num_list = list(map(int, input().split()))
# print(m, num_list)

card_list.sort()

result = ''

def binary_search(list, target):
  left = 0
  right = len(list) - 1

  while left <= right:
    center = (left + right) // 2

    if card_list[center] == num:
      return True
    elif card_list[center] < num:
      left = center + 1
    else:
      right = center - 1
  return False


for num in num_list:
  result = binary_search(card_list, num)
  if result:
    print(1, end=' ')
  else:
    print(0, end=' ')

# 이진탐색은 플래그를 사용하지 않고 함수로 만들것

