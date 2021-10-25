marble = input()
sum = 0
for i in range(len(marble)):
  if marble[i] == '1':
    sum += 1
    
print(sum)