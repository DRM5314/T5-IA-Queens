from Controller.Controller import Controller

controller = Controller(10)

counter = 0
controller.aceptacion()
while controller.itsTheBest():
    controller.aceptacion()
    controller.selectFathers()
    controller.mix(counter)
    counter += 1
    print(f'Interaction: {counter}, best aceptation is: {controller.showBestPoblation()}')