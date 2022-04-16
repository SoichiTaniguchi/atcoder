s = input()
flag = [True for i in range(10)]
for i in range(9):
  flag[int(s[i])]= False
  
for i in range(10):
  if flag[i]:
    print(i)