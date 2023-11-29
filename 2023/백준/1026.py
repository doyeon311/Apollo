# 보물
import sys

def input():
  return sys.stdin.readline()

# 길이가 n
# 배열 A 재정렬
# 배열 B 재정렬 x

# S = A[0]*B[0] + A[1]*B[1] + ... 
# S 의 최솟값

# 작은수는 큰수랑 큰수는 작은수랑

n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort(reverse=True)
b_list.sort()

s = 0
for i in range(n):
  s += a_list[i] * b_list[i]
# print(a_list, b_list)
print(s)