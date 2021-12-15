n, m = map(int, input().split())
b = [[0 for i in range(m)] for j in range(n)] 

for i in range(n):
  b[i] = list(map(int, input().split()))

x = [[0 for i in range(m)] for j in range(n)]
y = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
  for j in range(m):
    x[i][j] = int((b[i][j] - 1) / 7)
    y[i][j] = (b[i][j] - 1) % 7

can = 'Yes'
for i in range(n):
  for j in range(m):
    if i > 0 and x[i][j] != x[i-1][j]+1:
      can = 'No'
    if j > 0 and y[i][j] != y[i][j-1]+1:
      can = 'No'
    if j > 0 and x[i][j] != x[i][j-1]:
      can = 'No'
    if i > 0 and y[i][j] != y[i-1][j]:
      can = 'No'
print(can)