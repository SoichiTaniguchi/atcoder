n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = min(b) - max(a)
if count >= 0:
  print(count + 1)
else:
  print(0)