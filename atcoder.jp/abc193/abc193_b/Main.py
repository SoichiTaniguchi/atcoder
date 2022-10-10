n = int(input())
ans = 999999999
for i in range(n):
  a, p, x = map(int, input().split())
  if a < x:
    ans = min(p, ans)

if ans == 999999999:
  print(-1)
else:
  print(ans)