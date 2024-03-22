def fibo(x):
  print(x)
  if x == 1 or x == 2:
    return 1
  return fibo(x - 1) + fibo(x - 2)

print(fibo(3))

d = [0] * 101

def fibo(x):
  if x == 1 or x == 2:
    return 1

  if d[x] != 0:
    return d[x]
  
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]

print(fibo(100))

d = [0] * 101

d[1] = 1
d[2] = 1

for i in range(3, 101):
  d[i] = d[i-1] + d[i-2]
print(d[100])