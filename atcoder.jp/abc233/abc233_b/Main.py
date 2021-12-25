l, r = map(int, input().split())
s = input()

st = s[l-1:r]
st_inv = st[::-1]
stt = s[:l-1] + st_inv + s[r:]
print(stt)