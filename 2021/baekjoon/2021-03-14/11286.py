# 절댓값 힙
# https://www.acmicpc.net/problem/11286
import heapq
import sys


def input():
    return sys.stdin.readline()


n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    elif len(heap):
        num = heapq.heappop(heap)
        print(num[1])
    else:
        print(0)