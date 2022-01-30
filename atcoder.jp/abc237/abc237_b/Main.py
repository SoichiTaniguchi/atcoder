h, w = map(int, input().split())
b = [[0] * h for i in range(w)]
for i in range(h):
  a = list(map(int, input().split()))
  for j in range(w):
    b[j][i] = a[j]
  
for i in range(w):
  print(*b[i])