n = int(input())
s = []
for i in range(n):
  S = input()
  s.append(S)
  
for i in range(n):
    print(s[-(i + 1)])