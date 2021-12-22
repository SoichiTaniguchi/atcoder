a = input()
a_inv = a[::-1]
st = len(a)
x = a[:st-2]
y = a[st-1:]

ans = x
if 0 <= int(y) <= 2:
  ans += '-'
elif 7 <= int(y) <= 9:
  ans += '+'
print(ans)