# 중복 빼고 정렬하기
# set?
import sys

def input():
  return sys.stdin.readline()

n = int(input())

nums = list(map(int, input().split()))
filtered_nums = list(set(nums))

filtered_nums.sort()

print(' '.join(list(map(str, filtered_nums))))
