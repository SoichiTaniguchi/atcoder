a, b = map(int, input().split())
if a > 0 and b == 0:
  print('Gold')
if a == 0 and b > 0:
  print('Silver')
if a > 0 and b > 0:
  print('Alloy')