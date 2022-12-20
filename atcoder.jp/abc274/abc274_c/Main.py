n = int(input())
a = list(map(int, input().split()))
ans=[0]*(2*n+1)
for i,b in enumerate(a):
  ans[2*i+1]=ans[b-1]+1
  ans[2*i+2]=ans[b-1]+1
print(*ans,sep="\n")