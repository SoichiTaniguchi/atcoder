from collections import Counter
n = int(input())
a = list(map(int, input().split()))
res = 0
cnt = Counter(a)
ans = 0
for x in range(-200,201):
    for y in range(x+1,201):
        cx = cnt[x]
        cy = cnt[y]
        ans += cx*cy*(x-y)**2
print(ans)