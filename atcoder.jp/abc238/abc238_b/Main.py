N = int(input())
A = list(map(int, input().split()))
a = [0]
 
for i in A:
    a.append((a[-1]+i)%360)
 
a.append(360)
a.sort()
 
ans = a[0]
 
for i in range(len(a)-1):
    ans = max(ans, a[i+1]-a[i])
print(ans)