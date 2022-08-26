n = int(input())
cnt = dict()
for i in range(n):
  s = input()
  if not s in cnt:
    print(s)
    cnt[s] = 1
  else:
    print(f"{s}({cnt[s]})")
    cnt[s] += 1