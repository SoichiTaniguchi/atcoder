import sys
n = int(input())
k = 0
while 1:
  if 2**k > n:
    print(k-1)
    sys.exit()
  k += 1