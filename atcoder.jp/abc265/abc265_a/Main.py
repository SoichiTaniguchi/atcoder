x, y, n = map(int, input().split())
ans = 0
if 3*x > y:
  yy = int(n / 3)
  ans = y * yy + x * (n - yy*3)
else:
  ans = x * n
print(ans)