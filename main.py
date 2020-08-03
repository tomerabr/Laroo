from card import Card,Shape
from player import Player
import random

def giveCards():
    count = 0
    while count < 4:
        random.shuffle(cards)
        card = random.choice(cards)
        players[i-1].giveCard(card)
        cards.remove(card)
        count += 1

print("Please choose 4 or 6 players")
num_of_players = int(input())
while True:
    if num_of_players == 4 or num_of_players == 6:
        break
    print("Number of players is 4 or 6")
    num_of_players = int(input())

if num_of_players == 4: mincard = 7
else: mincard = 3

#init all the cards in the game
cards = []
for shape in Shape:   
    for i in range(mincard,15):
        card = Card(i,shape)
        cards.append(card)
        #card.printCard()

#init players with first 4 cards and then give another 4 cards
players = []
for i in range(1,num_of_players+1):
    players.append(Player())
    giveCards()
    
#choose hukum/do laru...

for i in range(1,num_of_players+1):
    giveCards()
    print("Player number " + str(i))
    players[i-1].printCards()

        
