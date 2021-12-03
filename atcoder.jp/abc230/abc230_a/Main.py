n = input()
if int(n) >= 42:
  n = str(int(n) + 1)
con = 'AGC'
if len(n) == 1:
  con = con + '00' + n
elif len(n) == 2:
  con = con + '0' + n
else:
  con = con + n
print(con)