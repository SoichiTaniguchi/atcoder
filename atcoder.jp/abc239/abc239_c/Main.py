x1, y1, x2, y2 = map(int, input().split())

for x in range(x1-2, x1+3):
  for y in range(y1-2, y1+3):
    dis1 = (x - x1) ** 2 + (y - y1) ** 2
    dis2 = (x - x2) ** 2 + (y - y2) ** 2
    if dis1 == dis2 == 5:
      print('Yes')
      exit()
    
print('No')