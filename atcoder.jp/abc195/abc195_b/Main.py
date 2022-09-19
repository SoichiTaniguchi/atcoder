import math

a, b, w = map(int, input().split())
u = int(math.floor(1000*w/a))
l = int(math.ceil(1000*w/b))

if l > u:
  print("UNSATISFIABLE")
else:
  print(l,u)