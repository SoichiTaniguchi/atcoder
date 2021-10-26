NUM  = int(input())
card = list(map(int, input().split()))

Alice = 0
Bob   = 0

card.sort(reverse=True)

for i in range(NUM):
  if i%2 == 0:
    Alice += card[i]
  else:
    Bob += card[i]
    
print(Alice - Bob)