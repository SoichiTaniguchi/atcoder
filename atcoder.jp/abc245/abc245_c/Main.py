n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [False] * (n)
ep = [False] * (n)
dp[0] = True
ep[0] = True

for i in range(1,n):
  if dp[i-1]:
    if abs(a[i-1] - a[i]) <= k:
      dp[i] = True
    if abs(a[i-1] - b[i]) <= k:
      ep[i] = True
  if ep[i-1]:
    if abs(b[i-1] - a[i]) <= k:
      dp[i] = True
    if abs(b[i-1] - b[i]) <= k:
      ep[i] = True
      
if dp[n-1] or ep[n-1]:
  print("Yes")
else:
  print("No")