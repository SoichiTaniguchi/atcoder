s = input()
n = len(s)

v = []
for i in range(n):
  v.append(s[i:n] + s[0:i])
  
print(min(v))
print(max(v))