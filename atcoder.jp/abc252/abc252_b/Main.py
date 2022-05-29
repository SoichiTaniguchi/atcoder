n, k = map(int, input().split())
a= list(map(int, input().split()))
b= list(map(int, input().split()))

m = max(a)
for i in range(k):
  if a[b[i]-1] == m:
    print("Yes")
    exit()
    
print("No")