S = ['']*3
for i in range(3):
  S[i] = input()
  
moji = ''
T = input()
for i in range(len(T)):
  j = int(T[i]) - 1
  moji += S[j]
  
print(moji)