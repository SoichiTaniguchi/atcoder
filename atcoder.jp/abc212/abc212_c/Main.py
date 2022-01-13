n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

aa = sorted(a)
bb = sorted(b)
ans = 1000000000
x = 0
y = 0
while x < n and y < m:
  ans = min(ans, abs(aa[x] - bb[y]))
  if aa[x] > bb[y]:
    y += 1
  else:
    x += 1
    
print(ans)