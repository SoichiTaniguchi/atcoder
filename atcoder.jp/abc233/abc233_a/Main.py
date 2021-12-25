import sys
x, y = map(int, input().split())

sa = y - x
if sa <= 0:
  print(0)
  sys.exit()
  
count = int(sa / 10)
if sa % 10 == 0:
  print(count)
else:
  print(count+1)