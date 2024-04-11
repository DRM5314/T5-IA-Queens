import random
class Poblation:
    gene = []
    name: ""
    aceptation = 0
    conflictsPositions = []

    def __init__(self,name):
        self.gene = [None]*8
        self.name = name
        for i in range(8):
            self.gene[i] = random.randint(0,7)

    def viewGen(self):
        print(self.gene)

    def setAceptation(self,aceptation):
        self.aceptation = aceptation

    def getAceptation(self):
        return self.aceptation

    def addConflictPosition(self,position):
        self.conflictsPositions.append(position)

    def showConvlict(self):
        for conflict in self.conflictsPositions:
            print(conflict)

    def showDetails(self):
        print(f'Name: {self.name}')
        print(f'Gene: {self.gene}')
        print(f'Aceptation: {self.aceptation}\n')