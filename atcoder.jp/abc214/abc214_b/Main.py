s, t = map(int, input().split())
count = 0
for a in range(101):
  for b in range(101):
    for c in range(101):
      i = a + b + c
      j = a * b * c
      if i <= s and j <= t:
        count += 1
print(count)