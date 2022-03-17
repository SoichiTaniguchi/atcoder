n, k = map(int, input().split())
f = {}
for _ in range(n):
  a, b = map(int, input().split())
  f[a] = f.get(a,0) + b
  
ff = sorted(f.items())

for i in range(len(ff)):
  if ff[i][0] > k:
    break
  else:
    k += ff[i][1]
    
print(k)