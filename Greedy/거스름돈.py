# 이코테 - 거스름돈
# 거스름돈 500 100 50 10
# N원을 거슬러 줄 때 거스름돈 동전의 최소 개수

n = int(input())
changes = [500, 100, 50, 10]
cnt = 0
for change in changes:
  # cnt = rest // change
  # result += cnt
  # rest -= cnt * change
  cnt += n // change
  n %= change

print(cnt)