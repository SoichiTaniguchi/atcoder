n, s, d = map(int, input().split())
for _ in range(n):
  x, y = map(int, input().split())
  if x < s:
    if y > d:
      print("Yes")
      exit()
      
print("No")