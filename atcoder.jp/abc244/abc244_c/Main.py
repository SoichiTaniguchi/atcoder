n = int(input())
used = [False] * (2*n+2)

ans = -1
while ans != 0:
  for i in range(1,2*n+2):
    if used[i] == False:
      print(i)
      used[i] = True
      break
      
  ans = int(input())
  used[ans] = True