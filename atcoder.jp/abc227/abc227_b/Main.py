N = int(input())
S = list(map(int, input().split()))
 
ans = 0
for s in S:
  next = False
  for a in range(1, 150):
    for b in range(1, 150):
      if 4*a*b + 3*a +3*b == s:
        next = True       
  if not next:
    ans += 1
    
print(ans)