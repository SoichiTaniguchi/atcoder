n, w = map(int, input().split())
a = list(map(int, input().split()))
check = [0] * (w+1)
for i in range(n):
  s = a[i]
  if s <= w:
    check[s] = 1
  for j in range(i+1,n):
    s = a[i] + a[j]
    if s <= w:
      check[s] = 1
    for k in range(j+1,n):
      s = a[i] + a[j] + a[k]
      if s <= w:
        check[s] = 1
        
ans = 0
for i in range(w+1):
  ans += check[i]
print(ans)