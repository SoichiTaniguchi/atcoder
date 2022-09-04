n = int(input())
a = list(map(int, input().split()))
for i in range(len(a)):
  a[i] -= 1
  
dp = [0] * n
for i in range(1,n):
  dp[i] = dp[a[i-1]]+1
  
print(dp[n-1])