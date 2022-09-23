n, m, t = map(int, input().split())
a = [0] + list(map(int, input().split()))
bonus = [0] * (n+1)
for i in range(m):
  x, y = map(int, input().split())
  bonus[x] = y
  
for i in range(1, n):
  if t <= a[i]:
    print("No")
    exit()
  t -= a[i]
  t += bonus[i+1]
print("Yes")