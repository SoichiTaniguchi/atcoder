n, m, t = map(int, input().split())
time = 0
charge = n
result = True
for i in range(m):
  a, b = map(int, input().split())
  charge -= (a-time)
  time = a
  if charge <= 0:
    result = False
    charge = 0
    
  charge += (b-time)
  time = b
  if charge >= n:
    charge = n
    
charge -= (t-time)
if charge <= 0:
  result = False
  charge = 0
  
print("Yes") if result else print("No")