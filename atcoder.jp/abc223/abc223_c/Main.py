n = int(input())
a = []
b = []
for i in range(n):
  A, B = map(int, input().split())
  a.append(A)
  b.append(B)
  
t = 0
ans = 0
for i in range(n):
  t += a[i] / b[i]
t /= 2

for i in range(n):
  ans += min(a[i], t * b[i])
  t -= min(a[i]/b[i], t)
  
print(ans)