a, b, c = map(int, input().split())
if a <= b and c >= b:
  print("Yes")
elif c <= b and a >= b:
  print("Yes")
else:
  print("No")