n = int(input())
s = ['']*n
for i in range(n):
  s[i] = input()
  
name = ''
count = 0

for i in range(n):
  kouho = s[i]
  kaz = 0
  for j in range(n):
    if s[j] == kouho:
      kaz += 1
  if kaz > count:
    count = kaz
    name = kouho
print(name)