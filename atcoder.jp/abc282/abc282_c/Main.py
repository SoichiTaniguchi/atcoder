n = int(input())
s = list(input())
lef_even = True
for i in range(n):
    if lef_even and s[i] == ",":
        s[i] = "."
    if s[i] == '"':
        lef_even = not lef_even
print("".join(s))