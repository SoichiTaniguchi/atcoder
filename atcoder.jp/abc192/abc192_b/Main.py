s = input()
Sodd = s[1::2]
Seven = s[::2]
flag = False
if len(s)==1:
  if s.islower():
    flag = True
else:
  if Seven.islower():
    if Sodd.isupper():
      flag = True
      
if flag:
  print("Yes")
else:
  print("No")