# 숫자카드 2
import sys

def input():
  return sys.stdin.readline()

n = int(input()) # max 500 000
cards = list(map(int, input().split())) # -10 000 000 -> 10 000 000
m = int(input())
nums = list(map(int, input().split()))

# nums의 숫자가 적힌 카드를 각각 몇개씩 가지고 있는지

# 1.
gap = 10000000
template = [0] * 20000001

for card in cards:
  template[card+gap] += 1

for num in nums:
  print(template[num+gap], end=" ")

# 2. 해시?
count_dict = {}

for card in cards:
  if card not in count_dict:
    count_dict[card] = 0
  count_dict[card] += 1

for num in nums:
  if num not in count_dict:
    print(0, end=" ")
  else:
    print(count_dict[num], end=" ")
