a, b, c = map(int, input().split())
#ac = a ** c
#bc = b ** c
if c%2 == 0:
  if abs(a) < abs(b):
    print("<")
  elif abs(a) > abs(b):
    print(">")
  elif abs(a) == abs(b):
    print("=")
else:
  if a < b:
    print("<")
  elif a > b:
    print(">")
  elif a == b:
    print("=")