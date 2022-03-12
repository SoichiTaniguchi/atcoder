v, a,b, c = map(int, input().split())
s = a + b +c
nn = v % s
if 0 <= nn < a:
  print('F')
elif a <= nn < a + b:
  print('M')
else:
  print('T')