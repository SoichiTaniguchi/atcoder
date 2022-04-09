n, k, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
  ans += a[i]
m = 0
for i in range(n):
  m += int(a[i]/x)
m = min(m, k)
ans -= m * x
k -= m

for i in range(n):
  a[i] = a[i] % x
a.sort(reverse=True)
for i in range(n):
  if k == 0:
    break
  ans -= a[i]
  k -= 1
  
print(ans)