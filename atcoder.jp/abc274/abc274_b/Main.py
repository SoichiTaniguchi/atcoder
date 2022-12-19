H,W=map(int,input().split())
answer=[0 for _ in range(W)]
for i in range(H):
    C=input()
    for j in range(W):
        if C[j]=='#':
            answer[j]+=1
print(' '.join([str(x) for x in answer]))