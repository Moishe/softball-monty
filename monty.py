import random

random.seed()

wins = [0,0]
for i in range(0,10000000):
    if i % 1000000 == 0:
        print str(i) + ": " + str(wins)

    winners = [0,0]
    for j in range(0,7):
        if j == 0 or j == 1:
            winners[0] += 1
        elif j == 5 or j == 6:
            winners[1] += 1
        else:
            winners[random.choice([0,1])] += 1

        if winners[0] == 4:
            wins[0] += 1
            break
        elif winners[1] == 4:
            wins[1] += 1
            break

print str(i) + ": " + str(wins)

