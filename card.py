from enum import Enum

class Shape(Enum):
    HEART = 1
    DIAMOND = 2
    SPADES = 3
    CLUBS = 4

    def __lt__(self,other):
        return self.value < other.value

class Card:
    def __init__(self, value, shape):
        self.value = value
        self.shape = shape

    def printCard(self):
        name = {
            11: "J",
            12: "Q",
            13: "K",
            14: "A",
        }.get(self.value,self.value)

        shape = {
            Shape.HEART: "♥",
            Shape.DIAMOND:"♦",
            Shape.SPADES:"♠",
            Shape.CLUBS:"♣",
        }[self.shape]

        print(name,shape, end=" ")

    def __lt__(self,other):
        return ((self.shape,self.value) < (other.shape,other.value))


