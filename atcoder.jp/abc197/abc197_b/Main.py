h, w, x, y = map(int, input().split())
s = ['']*h
for i in range(h):
  s[i] = input()
cnt = -3
for i in range(x-1,h):
  if s[i][y-1] == "#": break
  cnt += 1
for i in range(x-1,-1,-1):
  if s[i][y-1] == "#": break
  cnt += 1
for j in range(y-1,w):
  if s[x-1][j] == "#": break
  cnt += 1
for j in range(y-1,-1,-1):
  if s[x-1][j] == "#": break
  cnt += 1
  
print(cnt)