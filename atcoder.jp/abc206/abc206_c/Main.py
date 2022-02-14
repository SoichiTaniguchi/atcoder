n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
num = len(b)*(len(b)-1)/2
count = 1
for i in range(n-1):
  if b[i] == b[i+1]:
    count += 1
  else:
    num -= count * (count-1) /2
    count = 1
if count != 1:
  num -= count * (count-1) /2
print(int(num)) 