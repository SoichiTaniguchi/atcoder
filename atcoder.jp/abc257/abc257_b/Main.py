n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

for i in range(q):
  x = a[l[i]-1]
  if x != n:
    if x + 1 not in a:
      a[l[i]-1] = x + 1
    
for s in a:
  print(s, end =" ")