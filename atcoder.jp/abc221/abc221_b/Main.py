S = list(input())
T = list(input())

i = 0
can = True
change = 0

while i < len(S):
  if change > 1:
    break
  if S[i] == T[i]:
    i += 1
  else:
    buf = S[i]
    S[i] = S[i+1]
    S[i+1] = buf
    change += 1
      
if change <= 1:
  print('Yes')
else:
  print('No')