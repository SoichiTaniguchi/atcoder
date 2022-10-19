s = []
for i in range(10):
  s.append(list(input()))
  
a, b, c, d = 11, 0, 11, 0
for i in range(10):
    for j in range(10):
        if s[i][j] == '#':
            a = min(i + 1, a)
            b = max(i + 1, b)
            c = min(j + 1, c)
            d = max(j + 1, d)
print('{} {}'.format(a, b))
print('{} {}'.format(c, d))