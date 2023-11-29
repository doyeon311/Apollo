n, m = map(int, input().split())

# 어떤 식으로 자르던 항상 횟수는 똑같은듯?
# m과 n이 바뀌어도 횟수는 똑같음
# (m-1) + (n-1)*m

count = (m-1) + (n-1)*m

print(count)