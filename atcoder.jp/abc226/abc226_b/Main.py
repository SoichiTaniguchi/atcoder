n = int(input())
l = [0]
for i in range(n):
  a = list(map(int, input().split()))
  l.append(a)
l.remove(0)

l = list(map(list, set(map(tuple, l))))
print(len(l))