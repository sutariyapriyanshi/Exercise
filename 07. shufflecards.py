# python program to shuffle the deck of cards

import random,itertools
deck=list(itertools.product(range(1,14),["Spade","club","Heart","Diamond"])) # it means from 1 to 13
# print(deck)
random.shuffle(deck)
print(deck)

for i in range(3):
    print(deck[i][0],"of",deck[i][1])
