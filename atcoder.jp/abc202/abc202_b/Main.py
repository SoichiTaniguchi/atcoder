s = input()
t = []
for i in range(len(s)):
  if s[i] == '0' or s[i] == '1' or s[i] == '8':
    t.append(s[i])
  elif s[i] == '6':
    t.append('9')
  else:
    t.append('6')
t.reverse()
print("".join(t))