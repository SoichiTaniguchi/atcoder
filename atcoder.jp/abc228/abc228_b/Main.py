N, X = map(int, input().split())
A = list(map(int, input().split()))

B = [0]*N
next = X-1
B[next] = 1

for i in range(N):
  if B[A[next]-1] == 0:
    B[A[next]-1] = 1
    next = A[next]-1
  else:
    break

W = 0    
for i in range(N):
  if B[i] == 1:
    W += 1
    
print(W)