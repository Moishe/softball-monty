import random

random.seed()

wins = [0,0]
for i in range(0,10000000):
    winners = []
    for j in range(0,7):
        if j == 0 or j == 1:
            winner = 0
        elif j == 5 or j == 6:
            winner = 1
        else:
            winner = random.choice([0,1])
        winners.append(winner)

    if winners.count(0) >= 4:
        wins[0] += 1
    else:
        wins[1] += 1

    if i % 1000000 == 0:
        print wins

        
