N = int(input())
A = list(map(int, input().split()))
X = int(input())

SUM = sum(A)
  
count = X // SUM
sabun = count * SUM
COUNT = count * N

while sabun <= X:
  sabun += A[COUNT%N]
  COUNT += 1
    
print(COUNT)