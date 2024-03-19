# 시각

# 0h 0m 0s ~ Nh 59h 59s 까지 중 3이 하나라도 들어가 있는 경우의 수

n = int(input())
cnt = 0

for h in range(0, n + 1):
  for m in range(0, 60):
    for s in range(0, 60):
      if '3' in str(h) or '3' in str(m) or '3' in str(s):
        print(cnt,' -- ', h, m, s)
        cnt += 1

print(23 * 60 * 60,cnt)
