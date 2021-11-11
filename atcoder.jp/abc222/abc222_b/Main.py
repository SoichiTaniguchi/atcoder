N, P = map(int, input().split())
a = list(map(int, input().split()))

F = 0
for i in range(N):
  if a[i] < P:
    F += 1

print(F)