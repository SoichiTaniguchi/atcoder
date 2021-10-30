NUM  = int(input())

diameter = list(range(NUM))

for i in range(NUM):
  diameter[i] = int(input())

unique = list(set(diameter))
print(len(unique))