x=input()

point = x.find('.')
if x[point+1] < '5':
  num = int(x[0:point])
  print(num)
else:
  num = int(x[0:point]) + 1
  print(num)