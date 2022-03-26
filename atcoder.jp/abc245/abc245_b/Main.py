n = int(input())
a = list(map(int, input().split()))

aa = list(set(a))
count = 0
for i in range(2001):
  if count == len(aa):
    print(i)
    exit()
  if i == int(aa[count]):
    count += 1
  else:
    print(i)
    exit()