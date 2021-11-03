N = int(input())

top = [0]*N

for i in range(N-1):
  a, b = map(int, input().split())
  top[a-1] += 1
  top[b-1] += 1
  
can = False
for i in range(N):
  if top[i] == N-1:
    print('Yes')
    can = True
    
if can == False:
  print('No')