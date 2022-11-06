n, x = map(int, input().split())
val =0
for i in range(n):
  v, p = map(int, input().split())
  val += v*p
  if val > x*100:
    print(i+1)
    exit()
print(-1)