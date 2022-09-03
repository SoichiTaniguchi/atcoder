a = list(map(int, input().split()))
b = list(set(a))
if len(b) == 2:
  if a.count(b[0]) == 3 or a.count(b[0]) == 2:
    print("Yes")
    exit()
print("No")