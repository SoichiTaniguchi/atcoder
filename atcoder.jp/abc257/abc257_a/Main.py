n, x = map(int, input().split())
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if x%n == 0:
  print(a[int(x/n)-1])
else:
  print(a[int(x/n)])