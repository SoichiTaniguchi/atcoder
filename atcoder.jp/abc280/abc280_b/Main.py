n = int(input())
s = list(map(int, input().split()))
a = []
for i in range(n):
  temp = s[i]
  for j in range(i):
    temp -= a[j]
  a.append(temp)

print(*a)