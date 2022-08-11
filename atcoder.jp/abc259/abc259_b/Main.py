import math
a, b, d = map(int, input().split())
r = math.hypot(a, b)
theta = math.atan2(b,a)

theta += d * math.acos(-1.0)/180
x = math.cos(theta) * r
y = math.sin(theta) * r

print(x, y)