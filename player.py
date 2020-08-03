from card import Card

class Player:
    def __init__(self):
        self.cards = []
        #is doing laru
        #team

    def giveCard(self,card):
       self.cards.append(card)

    def printCards(self):
        for card in self.cards:
            card.printCard()