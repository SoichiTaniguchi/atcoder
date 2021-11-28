a, b = map(str, input().split())

for i in range(min(len(a), len(b))):
  if int(a[-i-1]) + int(b[-i-1]) >= 10:
    print('Hard')
    exit()

print('Easy')