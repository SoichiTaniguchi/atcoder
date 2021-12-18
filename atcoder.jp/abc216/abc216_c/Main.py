n = int(input())
ans = ''
while n > 0:
  if n % 2 != 0:
    ans += 'A'
    n -= 1
  else:
    ans += 'B'
    n = n//2
print(ans[::-1])