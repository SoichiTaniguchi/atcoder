n = int(input())
a = []
for i in range(n):
  A = input()
  AA = []
  for j in range(len(A)):
    AA.append(A[j])
  a.append(AA)
  
p = [1,1,1,0,0,-1,-1,-1]
q = [1,0,-1,1,-1,1,0,-1]

ans = 0
for i in range(n):
  for j in range(n):
    for k in range(8):
      now = 0
      x = i
      y = j
      for l in range(n):
        now *= 10
        now += int(a[x][y])
        x += p[k]
        y += q[k]
        x %= n
        x += n
        y %= n
        y += n
        x %= n
        y %= n
      ans = max(ans, now)
print(ans)