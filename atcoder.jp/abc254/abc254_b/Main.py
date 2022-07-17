n = int(input())
a = [1]
for i in range(n):
  print(*a)
  b = [1]
  for j in range(i):
    b.append(a[j] + a[j+1])
  b.append(1)
  a = b