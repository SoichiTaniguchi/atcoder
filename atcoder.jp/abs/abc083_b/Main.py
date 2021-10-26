N, A, B = map(int, input().split())
total_sum = 0

for num in range(1, N+1):
  sum = 0
  N_str = ""
  N_str = str(num)
  for i in range(len(N_str)):
    sum += int(N_str[i])
    
  if A <= sum <= B:
    total_sum += num
    
print(total_sum)