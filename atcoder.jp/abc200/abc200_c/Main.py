import math

n = int(input())
a = list(map(int, input().split()))

b = []
for i,v in enumerate(a):
  b.append(v%200)
  
dict = {}
for i,v in enumerate(b):
  if v not in dict:
    dict[v] = 1
  else:
    dict[v]+=1
    
ans = 0

for i,v in dict.items():
  if v >= 2:
    ans+=math.comb(v,2)
 
print(ans)