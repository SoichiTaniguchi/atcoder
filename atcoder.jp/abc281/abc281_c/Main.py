n, t = map(int, input().split())
a = list(map(int, input().split()))
total = 0
for A in a:
  total += A
  
t = t % total
count = 1
for A in a:
  if t < A:
    print(count, t)
    exit()
  else:
    t -= A
    count += 1