n, k = map(int, input().split())
a = list(map(int, input().split()))
b = k//n
k %= n
c = [(a[i], i) for i in range(n)] #辞書で保存
ans = [0] * n
c.sort()

for i in range(n):
  a, j = c[i]
  if i < k:
    ans[j] = b + 1
  else:
    ans[j] = b
for i in ans:
  print(i)