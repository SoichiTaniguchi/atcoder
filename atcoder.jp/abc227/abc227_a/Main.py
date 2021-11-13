N, K, A = map(int, input().split())

now = A - 1
for i in range(K):
  if now == N:
    now = 0
  now += 1
    
print(now)