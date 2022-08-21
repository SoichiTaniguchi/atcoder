n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
flag = [False] * 1010

for _ in range(x):
  pos = -1
  for i in range(n):
    if flag[i] == False:
      if pos == -1 or a[i] > a[pos]:
        pos = i
  flag[pos] = True
  
for _ in range(y):
  pos = -1
  for i in range(n):
    if flag[i] == False:
      if pos == -1 or b[i] > b[pos]:
        pos = i
  flag[pos] = True
  
for _ in range(z):
  pos = -1
  for i in range(n):
    if flag[i] == False:
      if pos == -1 or a[i]+b[i] > a[pos]+b[pos]:
        pos = i
  flag[pos] = True
  
for i in range(n):
  if flag[i]:
    print(i+1)