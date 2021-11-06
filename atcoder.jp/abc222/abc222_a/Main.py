N = str(input())
zero = 4 - len(N)

out = ''
for i in range(zero):
  out += '0'
  
out += N
print(out)