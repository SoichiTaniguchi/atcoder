n, x = map(int, input().split())
a = list(map(int, input().split()))

aa = a[0::2]
for i in a[1::2]:
  aa.append(i-1)

s = sum(aa)
if s <= x:
  print('Yes')
else:
  print('No')