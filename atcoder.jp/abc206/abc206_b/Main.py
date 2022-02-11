n = int(input())
i = 1
count = 0
while 1:
  count += i
  if count >= n:
    print(i)
    exit()
  i += 1