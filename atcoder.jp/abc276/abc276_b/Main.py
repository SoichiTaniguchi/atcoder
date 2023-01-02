n,m = map(int,input().split())
vertex =[[] for _ in range(n+1)]
 
for _ in range(m):
  a,b = map(int,input().split())
  vertex[a].append(b)
  vertex[b].append(a)
  
for i in range(1,n+1):
  vertex[i].sort()
  print(len(vertex[i]),*vertex[i])