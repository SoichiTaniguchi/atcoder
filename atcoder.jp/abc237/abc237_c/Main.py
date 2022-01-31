s = input()
x = 0
for i in s:
  if i == 'a':
    x += 1
  else:
    break
    
y = 0
for i in s[::-1]:
  if i == 'a':
    y += 1
  else:
    break

if x > y:
  print('No')
  exit()
elif x == y:
  if s == s[::-1]:
    print("Yes")
  else:
    print("No")
else:
  s = s[::-1]
  s = s + ('a' * (y - x))
  if s == s[::-1]:
    print('Yes')
  else:
    print('No')