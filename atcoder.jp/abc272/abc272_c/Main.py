n = int(input())
lol = list(map(int, input().split(" ")))
 
even = []
odd = []
for l in lol:
    if l % 2 == 0: even.append(l)
    else: odd.append(l)
 
even.sort()
odd.sort() 
sum1 = -1
if len(even) > 1:
    sum1 = even[-1] + even[-2]
sum2 = -1
if len(odd) > 1:
    sum2 = odd[-1] + odd[-2] 
 
answer = max(sum1, sum2)
print(answer)