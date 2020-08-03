class Team:
    def _init_(self):
        self.points = 0
        self.packs = 0 #packs won
        self.hukum = false
        
        #players
        #is doing laru

    def resetPacks(self):
        self.packs = 0

    def changeHukumTeam(self):
        self.hukum = not self.hukum

    #points can be both positive or negative
    def changePoints(self,points):
        self.points += points

    def checkWon(self):
        if self.hukum and self.packs == 5:
            return True
        elif not self.hukum and self.packs == 4:
            return True
        return False