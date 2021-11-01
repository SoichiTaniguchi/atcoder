A, B, C = map(int, input().split())
max = int(B/C)
can = False

for i in range(max):
  D = C * (i +1)
  if A <= D <= B:
    print(D)
    can = True
    break
    
if can == False:
  print(-1)