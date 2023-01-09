first = ['H' , 'D' , 'C' , 'S']
second = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
s = []
n = int(input())
for i in range(n):
  S = input()
  ans = False
  if S[0] in first:
    if S[1] in second:
      if S not in s:
        ans = True
        s.append(S)
  if ans == False:
    print('No')
    exit()
print('Yes')