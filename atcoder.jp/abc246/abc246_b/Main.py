import math
a, b = map(int, input().split())
length = math.sqrt(pow(a,2)+pow(b,2))
print(a/length, b/length)