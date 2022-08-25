n = int(input())
a = [''] * n
for i in range(n):
  a[i] = input()
  
for i in range(n):
  for j in range(n):
    if i != j:
      if a[i][j] == "W" and a[j][i] != "L":
        print('incorrect ')
        exit()
      if a[i][j] == "L" and a[j][i] != "W":
        print('incorrect ')
        exit()
      if a[i][j] == "D" and a[j][i] != "D":
        print('incorrect ')
        exit()
      
print('correct')