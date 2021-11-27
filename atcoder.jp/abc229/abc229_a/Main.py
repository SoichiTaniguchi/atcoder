s1 = input()
s2 = input()

can = False
if s1[0] == '#' and s1[1] == '#':
  can = True
if s2[0] == '#' and s2[1] == '#':
  can = True
if s1[0] == '#' and s2[0] == '#':
  can = True
if s1[1] == '#' and s2[1] == '#':
  can = True
  
if can:
  print('Yes')
else:
  print('No')