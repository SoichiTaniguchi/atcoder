h, w = map(int, input().split())
a = [[0]*w]*h
for i in range(h):
  a[i] = list(map(int, input().split()))
  
for i_1 in range(h):
  for i_2 in range(i_1+1,h):
    for j_1 in range(w):
      for j_2 in range(j_1+1,w):
        if a[i_1][j_1]+a[i_2][j_2] > a[i_2][j_1]+a[i_1][j_2]:
          print('No')
          exit()
        
print('Yes')