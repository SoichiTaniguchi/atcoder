a, b, c, d, e, f = map(int, input().split())
ABC = a * b * c
DEF = d * e * f
print((ABC - DEF) % 998244353)