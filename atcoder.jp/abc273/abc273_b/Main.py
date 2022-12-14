x, k = map(int, input().split())
for i in range(k+1):
  x = round(x+0.5, -i)
  
print(int(x))