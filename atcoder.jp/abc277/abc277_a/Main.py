n, x = map(int, input().split())
p = list(map(int, input().split()))
for P in p:
  if P == x:
    print(p.index(P)+1)
    exit()