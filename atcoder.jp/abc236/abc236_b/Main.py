n = int(input())
a = list(map(int, input().split()))
kei = sum(range(1,n+1))*4
ll = sum(a)
ss = kei - ll
print(ss)