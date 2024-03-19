# 거스름돈

# 500원 100원 50원 10원
# 거슬러줘야 할 최소 동전 개수
# O(K)

def charge(money):
  cnt = 0
  coins = [500, 100, 50, 10]

  for coin in coins:
    cnt += money // coin
    money %= coin
  
  return cnt

print(charge(1260))

