import math

n, k = map(int, input().split())
a = list(map(int, input().split()))
x = []
y = []
for i in range(n):
  X, Y = map(int, input().split())
  x.append(X)
  y.append(Y)
  
res = 0
for i in range(n):
  cros = 8e18
  for nx in a:
    rr = float((x[i]-x[nx-1])*(x[i]-x[nx-1]) + (y[i]-y[nx-1])*(y[i]-y[nx-1]))
    cros = min(cros, rr)
    
  res = max(res, cros)
  
print(math.sqrt(res))