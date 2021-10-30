NUM, SUM = map(int,input().split())
result = [-1, -1, -1]

for i in range(NUM+1):
  for j in range(NUM+1-i):
    k = NUM - i - j
    sum = 10000*i + 5000*j + 1000*k
    if sum == SUM:
      result = [i, j, k]
      
print(*result)