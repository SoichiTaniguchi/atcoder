n = input()
for i in range(10):
  nn = "0"*i + n
  if nn == nn[::-1]:
    print("Yes")
    exit()
    
print("No")