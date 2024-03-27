# N과 M(7)
# N개의 자연수와 자연수 M
# 길이가 M인 수열을 모두 고르는 프로그램

# N 개의 자연수 중에 M개를 고른 수열
# 같은 수를 여러번 골라도 됨

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort()

selected = [False] * (n)

def back_tracking(selected_nums):
  if len(selected_nums) == m:
    print(' '.join(map(str, selected_nums)))
    return

  for i in range(n):
    back_tracking(selected_nums + [n_list[i]])

back_tracking([])