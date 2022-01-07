x = input()

if x[0] == x[1] == x[2] == x[3]:
  print('Weak')
  exit()
  
n = int(x[0]) + 1
can = True
for i in range(1,4):
  if n == 10:
    n = 0
  if int(x[i]) == n:
    n += 1
  else:
    can = False
    break;

if can:
  print('Weak')
else:
  print('Strong')