n = int(input())
c = list(map(int, input().split()))

c.sort()
count = 1
for i in range(n):
  count = count * max(0, c[i] - i) % 1000000007
  
print(count)