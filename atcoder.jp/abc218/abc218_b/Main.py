p = list(map(int, input().split()))

mozi=['']*26
for i in range(26):
  print(chr(p[i]+96), end='')