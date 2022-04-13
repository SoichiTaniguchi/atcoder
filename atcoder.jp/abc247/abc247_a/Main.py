s = input()
t = []
t.append('0')
for i in range(3):
  t.append(s[i])
  
print("".join(map(str, t)))