h, w = map(int, input().split())
r, c = map(int, input().split())
count = 0
if h == 1:
  count = count
elif 1 == r or h == r:
  count += 1
else:
  count += 2
  
if w == 1:
  count = count
elif 1 == c or w == c:
  count += 1
else:
  count += 2
  
print(count)