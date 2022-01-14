n, a, x, y = map(int, input().split())
total = 0
if a < n:
  total += a * x
  total += (n - a) * y
else:
  total += n * x
  
print(total)