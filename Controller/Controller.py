import Model.Poblation as Poblation
class Controller:
    max = 7
    initPoblation = []

    def __init__(self,initialPoblationEntry):
        for i in range(initialPoblationEntry):
            self.initPoblation.append(Poblation.Poblation("Poblation"+str(i)))

    def aceptacion(self):
        aceptation = 0
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
                    else:
                        genEntry.addConflictPosition(f'Conflicto en [{xPlus}, {gen[xPlus]}], Usando [{x},{gen[x]}]')
                else:
                    genEntry.addConflictPosition(f'Conflicto en [{xPlus}, {gen[xPlus]}], Usando [{x},{gen[x]}]')
        return returns

    def showDetails(self):
        for poblation in self.initPoblation:
            poblation.showDetails()

    def getSumAceptation(self):
        returns = 0
        for value in self.initPoblation:
            returns += value.getAceptation()

        return returns