import itertools
s, k = input().split()

p = set()
for c in itertools.permutations(s):
  p.add("".join(c))
                      
pp = sorted(p)
print(pp[int(k)-1])