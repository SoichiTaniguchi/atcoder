n = int(input())
t = input()

x, y, d = 0, 0, 0
for i in range(n):
  if t[i] == 'S':
    if d == 0:
      x += 1
    if d == 1:
      y -= 1
    if d == 2:
      x -= 1
    if d == 3:
      y += 1
  if t[i] == 'R':
    d = (d+1)%4
    
print(x,y)