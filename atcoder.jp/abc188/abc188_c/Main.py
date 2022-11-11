n = int(input())
a = list(map(int, input().split()))
x = int(2 ** n / 2)
b = a[:x]
c = a[x:]
b_max = max(b)
c_max = max(c)
if b_max < c_max:
  print(b.index(b_max)+1)
else:
  print(x + c.index(c_max)+1)