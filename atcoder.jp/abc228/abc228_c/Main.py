N, K = map(int, input().split())
P = [0] * N
for i in range(N):
  P[i] = sum(map(int, input().split()))
 
new = sorted(P, reverse=True)[K-1];
for x in P:
  print("Yes" if x+300 >= new else "No")