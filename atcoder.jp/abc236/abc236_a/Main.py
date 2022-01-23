s = input()
a, b = map(int, input().split())
aa = s[a-1]
bb = s[b-1]
ss = s[:a-1] + bb + s[a:b-1] + aa + s[b:]
print(ss)