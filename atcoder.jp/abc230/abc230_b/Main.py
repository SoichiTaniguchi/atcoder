s = input()
count = int(len(s)/3)
nokori = len(s)%3

a = ''
b = ''
c = ''
if s[0:2] == 'ox':
  a = 'oxx'
  b = 'ox'
  c = 'o'
elif s[0:2] == 'xx':
  a = 'xxo'
  b = 'xx'
  c = 'x'
else:
  a = 'xox'
  b = 'xo'
  c = 'x'
  
if len(s) == 1:
  print('Yes')
  exit()

for i in range(count):
  if s[0+3*i:3+3*i] != a:
    print('No')
    exit()
    
if nokori == 2:
  start = 3*count
  if s[start:start+nokori] != b:
    print('No')
    exit()
elif nokori == 1:
  if s[count:count+nokori] != c:
    print('No')
    exit()
    
print('Yes')