S, T, X = map(int, input().split())
if S <= T:
  if S > X:
    print('No')
  elif S <= X < T:
    print('Yes')
  else:
    print('No')
    
else:
  if T > X:
    print('Yes')
  elif T <= X < S:
    print('No')
  else:
    print('Yes')