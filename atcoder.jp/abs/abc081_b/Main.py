num = int(input())
number = list(map(int, input().split()))

max_change = 0
is_try = True

while is_try:
  max_change += 1
  for i in range(num):
    if number[i] % 2 == 0:
      number[i] = number[i]/2
    else:
      is_try = False
  
print(max_change-1)