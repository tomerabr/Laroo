from card import Card
import bisect

class Player:
    def __init__(self):
        self.cards = []
        #is doing laru
        #team
        #name

    def giveCard(self,card):
       bisect.insort(self.cards, card)

    def printCards(self):
        for card in self.cards:
            card.printCard()
        print()

    #def sortCards(self):
     #   self.cards.sort()