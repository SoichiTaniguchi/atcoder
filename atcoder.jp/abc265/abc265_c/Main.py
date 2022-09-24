h, w = map(int, input().split())
g = [list(list(input())) for _ in range(h)]
vis = [[False] * w for i in range(h)]

i = 0
j = 0
while(1):
  if vis[i][j]:
    print(-1)
    exit()
  vis[i][j] = True
  if g[i][j] == "U" and i != 0:
    i -= 1
  elif g[i][j] == "D" and i != h-1:
    i += 1
  elif g[i][j] == "L" and j != 0:
    j -= 1
  elif g[i][j] == "R" and j != w-1:
    j += 1
  else:
    break
    
print(i+1, j+1)