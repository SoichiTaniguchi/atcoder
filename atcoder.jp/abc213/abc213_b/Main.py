n = int(input())
a = list(map(int, input().split()))
aa = sorted(a)
for i in range(n):
  if a[i] == aa[n-2]:
    print(i+1)