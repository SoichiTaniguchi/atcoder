s = input()

big = False
small = False
for i in s:
  if i.isupper():
    big = True
  else:
    small = True
  
diff = True
for i in range(len(s)):
  for j in range(i+1,len(s)):
    if s[i] == s[j]:
      diff = False

if big and small and diff:
  print("Yes")
else:
  print("No")