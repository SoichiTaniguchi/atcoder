r, c = map(int, input().split())
A = []
for i in range(2):
  a = list(map(int, input().split()))
  A.append(a)
  
print(A[r-1][c-1])