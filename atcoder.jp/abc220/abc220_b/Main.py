K = int(input())
_A, _B = map(str, input().split())

A = 0
B = 0
lA = len(_A)
lB = len(_B)

for i in reversed(range(lA)):
  A += (K ** i) * int(_A[lA-i-1])
  
for i in reversed(range(lB)):
  B += (K ** i) * int(_B[lB-i-1])
  
print(A*B)