s = input()
for i in range(len(s), 0, -1):
  if s[i-1] == "a":
    print(i)
    exit()
print("-1")