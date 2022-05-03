N, K = map(int, input().split())
X = 'abcdefghijklmnopqrstuvwxyz'
Y = [0 for b in range(len(X))]
S = ['' for a in range(N)]
Ans = 0
for h in range(N):
    S[h] = input()
 
for i in range(2**N):
    SSS = ''
    for j in range (N):
        if (i>>j) & 1 :
            SSS = SSS + S[j]
    for k in range(len(X)):
        Y[k]=SSS.count(X[k])
    Ans = max(Ans, Y.count(K))
print(Ans)