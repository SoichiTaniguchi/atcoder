S = input()
uniqu =  ''.join(set(S))

if len(uniqu) == 1:
  print(1)
elif len(uniqu) == 2:
  print(3)
elif len(uniqu) == 3:
  print(6)