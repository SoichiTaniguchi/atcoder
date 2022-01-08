n = int(input())
xy = [[0 for j in range(2)] for i in range(n)]
for i in range(n):
  xy[i][0], xy[i][1] = map(int, input().split())
  
max = 0
for i in range(n-1):
  for j in range(i+1,n):
    dx = xy[i][0] - xy[j][0]
    dy = xy[i][1] - xy[j][1]
    l = ((dx ** 2 + dy ** 2) ** 0.5)
    if l > max:
      max = l
print(max)