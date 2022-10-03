X = []
Y = []
for _ in range(4):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    
def f0(x, y):
    return (X[2] - X[0]) * (y - Y[0]) - (Y[2] - Y[0]) * (x - X[0])
def f1(x, y):
    return (X[3] - X[1]) * (y - Y[1]) - (Y[3] - Y[1]) * (x - X[1])
def sgn(x):
    if x == 0:
        return 0
    return x // abs(x)
if sgn(f0(X[1], Y[1])) != sgn(f0(X[3], Y[3])) and sgn(f1(X[0], Y[0])) != sgn(f1(X[2], Y[2])):
    print("Yes")
else:
    print("No")