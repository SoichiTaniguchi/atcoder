a, b, c, d, e, f, x = map(int, input().split())
 
taka = int(x/(a+c)) * a * b
aoki = int(x/(d+f)) * d * e
 
ta = x % (a+c)
ao = x % (d+f)
if ta < a:
  taka += ta * b
else:
  taka += a * b
if ao < d:
  aoki += ao * e
else:
  aoki += d * e
  
if taka > aoki:
  print("Takahashi")
elif taka < aoki:
  print("Aoki")
else:
  print("Draw")