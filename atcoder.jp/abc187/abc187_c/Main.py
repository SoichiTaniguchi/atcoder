n = int(input())
s = set(input() for i in range(n))
  
for t in s:
  if "!" + t in s:
    print(t)
    exit()
print("satisfiable")