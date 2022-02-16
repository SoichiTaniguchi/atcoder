def search(a, n, x, cnt=0, pro=1):
  global ans
  
  #試行回数が最大以内の時
  if cnt != n:
    for i in a[cnt]:
      search(a, n, x, cnt+1, pro*i)
  
  #試行回数が最大で積がxの時
  elif pro == x:
    ans += 1

a = []
n, x = map(int, input().split())
for i in range(n):
  l = list(map(int, input().split()))[1:]
  a.append(l)
  
ans = 0
search(a, n, x)
print(ans)