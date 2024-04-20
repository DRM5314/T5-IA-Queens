import Model.Poblation as Poblation
import random
class Controller:
    max = 7
    initPoblation = []
    selectFathersList = []
    findSolution = True

    def __init__(self,initialPoblationEntry):
        for i in range(initialPoblationEntry):
            self.initPoblation.append(Poblation.Poblation("Poblation"+str(i)))

    def itsTheBest(self):
        for poblacion in self.initPoblation:
            if poblacion.getAceptation() >= 28:
                print("This is the best solution!! ")
                print(poblacion.showDetails())
                return False
        return True

    def byAceptation(self,poblacion):
        return poblacion.getAceptation()
    def mix(self,interaction):
        firstGroup = int (60*len(self.initPoblation)/100)
        new_generation = []
        new_generation.extend(self.initPoblation[:firstGroup])
        firstGroup = int(40 * len(self.initPoblation) / 100)

        for i in range(firstGroup):
            patern1 = random.choice(self.selectFathersList)
            patern2 = random.choice(self.selectFathersList)
            childChromosome = []
            randGenPos = random.randint(0,7)
            childChromosome.extend(patern1.gene[randGenPos:])
            childChromosome.extend(patern2.gene[:randGenPos])
            newChild = Poblation.Poblation("Child "+str(interaction+i))
            newChild.gene = childChromosome
            newChild = self.mutation(newChild)

            new_generation.append(newChild)

        self.initPoblation = new_generation

    def mutation(self,newChild):
        randGenPos = random.randint(0, 7)
        newChild.gene[randGenPos] = random.randint(0, 7)
        return newChild


    def aceptacion(self):
        for poblacion in self.initPoblation:
            aceptation = self.analize(poblacion)
            poblacion.setAceptation(aceptation)
    def analize(self, genEntry):
        gen = genEntry.gene
        returns = 0
        posAnt = 0
        for x in range(len(gen)):
            posAnt = x + 1
            if(posAnt == len(gen)):
                continue
            postResInt = 0
            for xPlus in range(posAnt, len(gen)):
                postResInt = postResInt + 1
                if gen[x] != gen[xPlus]:
                    if gen[x] != (gen[xPlus] + postResInt) and gen[x] != (gen[xPlus] - postResInt):
                        returns += 1
                #     else:
                #         genEntry.addConflictPosition(f'Conflicto en [{xPlus}, {gen[xPlus]}], Usando [{x},{gen[x]}]')
                # else:
                #     genEntry.addConflictPosition(f'Conflicto en [{xPlus}, {gen[xPlus]}], Usando [{x},{gen[x]}]')
        return returns

    def showDetails(self):
        for poblation in self.initPoblation:
            poblation.showDetails()

    def getSumAceptation(self):
        returns = 0
        for value in self.initPoblation:
            returns += value.getAceptation()
        return returns
    def selectFathers(self):
        numberFathersSelected = 0
        sumatory = 0
        while numberFathersSelected <= 10:
            numberAleatory = random.randint(0, self.getSumAceptation())
            # print(f'Number aleatory for select = {numberAleatory} \n')
            for poblation in self.initPoblation:
                sumatory += poblation.getAceptation()
                if sumatory >= numberAleatory:
                    # print(f'Father select is: {poblation.name}, and sum is: {sumatory}')
                    self.selectFathersList.append(poblation)
                    numberFathersSelected += 1
                    sumatory = 0
                    break
        self.initPoblation.sort(key=self.byAceptation, reverse=True)
    def showAllFathers(self):
        if len(self.selectFathersList) > 0:
            for poblation in self.initPoblation:
                poblation.showDetails()


    def showBestPoblation(self):
        if len(self.initPoblation) > 0:
            return f' Aceptation: {self.initPoblation[0].getAceptation()}, gene is: {self.initPoblation[0].gene}'
