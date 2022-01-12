s = [''] * 4
for i in range(4):
  s[i] = input()
  
if len(s) != len(set(s)):
  print('No')
else:
  print('Yes')