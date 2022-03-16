n, k = map(int, input().split())

s = 0
for i in range(1,n+1):
  for j in range(1,k+1):
    s += (100 * i + j)
    
print(s)