h, w, n = map(int, input().split())
a = []
b = []
for i in range(n):
  aa, bb = map(int, input().split())
  a.append(aa)
  b.append(bb)

x = {a:i+1 for i, a in enumerate(sorted(set(a)))}
y = {b:i+1 for i, b in enumerate(sorted(set(b)))}

for i in range(n):
  print(x[a[i]], y[b[i]])