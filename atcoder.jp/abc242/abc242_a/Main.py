a, b, c, x = map(int, input().split())
number = 0
if x <= a:
  number = 1
elif a < x <= b:
  number = c / (b-a)
else:
  number = 0
print(number)