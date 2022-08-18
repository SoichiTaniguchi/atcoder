n = int(input())
s = list(input())
q = int(input())
revflag=False

for _ in range(q):
  t, a, b = map(int, input().split())
  if t == 1:
    if revflag:
      if a-1<n: a+=n
      else: a-=n
      if b-1<n: b+=n
      else: b-=n
    s[a-1],s[b-1]=s[b-1],s[a-1]
  else: revflag^=True
    
if revflag: print("".join(s[n:]+s[:n]))
else: print("".join(s))