n, w = map(int, input().split())
v = [[0]*2]*n
for i in range(n):
  v[i] = list(map(int, input().split()))
v.sort(reverse=True)

omosa = 0
umami = 0
for a,b in v:
  if omosa +b > w:
    umami += a*(w-omosa)
    break
  omosa += b
  umami += a*b
print(umami)