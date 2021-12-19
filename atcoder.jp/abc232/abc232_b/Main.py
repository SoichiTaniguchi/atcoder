import sys
s = input()
t = input()

if ord(t[0]) < ord(s[0]):
  a = 26 + ord(t[0]) - ord(s[0])
else:
  a = ord(t[0]) - ord(s[0])

for i in range(1,len(s)):
  if ord(t[i]) < ord(s[i]):
    if 26 + ord(t[i]) - ord(s[i]) != a:
      print('No')
      sys.exit()
  else:
    if ord(t[i]) - ord(s[i]) != a:
      print('No')
      sys.exit()
    
print('Yes')