def aa(n):
  if n == 1:
    return [1]
  else:
    return aa(n-1) + [n] + aa(n-1)

n = int(input())
print(*aa(n))