n , m = map(int, input().split())
s = list(map(str, input().split()))
t = list(map(str, input().split()))

count1 = 0
count2 = 0
while count1 < n:
  if s[count1] == t[count2]:
    print('Yes')
    count1 += 1
    count2 += 1
  else:
    print('No')
    count1 += 1