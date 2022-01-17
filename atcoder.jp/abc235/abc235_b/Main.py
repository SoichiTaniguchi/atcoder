n = int(input())
h = list(map(int, input().split()))

now = 0
while True:
  if now == n-1:
    break
  else:
    if h[now] < h[now+1]:
      now += 1
    else:
      break
print(h[now])