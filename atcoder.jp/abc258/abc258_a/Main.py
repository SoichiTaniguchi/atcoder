k = int(input())
hh = str(21 + int(k/60))
if k % 60 < 10:
  mm = "0" + str(k%60)
else:
  mm = str(k%60)
time = hh + ":" + mm
print(time)