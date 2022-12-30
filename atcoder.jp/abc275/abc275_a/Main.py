n = int(input())
h = list(map(int, input().split()))
if n == 1:
  print(1)
else:
  print(h.index(sorted(h)[-1])+1)