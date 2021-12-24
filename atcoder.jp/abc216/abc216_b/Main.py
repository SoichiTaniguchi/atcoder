import sys
n = int(input())
s = [''] * n
t = [''] * n
for i in range(n):
  s[i], t[i] = map(str, input().split())
  
for i in range(n-1):
  for j in range(i+1,n):
    if s[i] == s[j]:
      if t[i] == t[j]:
        print('Yes')
        sys.exit()
print('No')