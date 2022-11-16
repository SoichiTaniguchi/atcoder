n = int(input())
a = [tuple(map(int, input().split())) for i in range(n)]
ans = 0

for i in range(n):
  for j in range(i):
    if abs(a[i][1] - a[j][1]) <= abs(a[i][0] - a[j][0]):
      ans += 1
      
print(ans)