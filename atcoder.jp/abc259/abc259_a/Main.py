N, M, X, T, D = map(int, input().split())

O = T - N * D
if M >= X:
  print(T)
else:
  print(T-(X-M)*D)