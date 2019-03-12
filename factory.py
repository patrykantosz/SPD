import dataClass


class Factory:
    def __init__(self):
        self.twoMachines = []
        self.threeMachines = []

    def startProduction(self, reader):
        print(reader.machines)
        if reader.machines == 2:
            for j in range(0, len(reader.machinesInFactory) - 1, 2):
                productionLine = dataClass.TwoMachinesTask(reader.machinesInFactory[j], reader.machinesInFactory[j + 1])
                self.twoMachines.append(productionLine)
        elif reader.machines == 3:
            for j in range(0, len(reader.machinesInFactory) - 1, 3):
                productionLine = dataClass.ThreeMachinesTask(reader.machinesInFactory[j],
                                                             reader.machinesInFactory[j + 1],
                                                             reader.machinesInFactory[j + 2])
                self.threeMachines.append(productionLine)

    def print(self):
        print("")
        if len(self.twoMachines) is not 0:
            for i in range(len(self.twoMachines)):
                print(self.twoMachines[i].timeOnFirstMachine, self.twoMachines[i].timeOnSecondMachine)
        else:
            for i in range(len(self.threeMachines)):
                print(self.threeMachines[i].timeOnFirstMachine, self.threeMachines[i].timeOnSecondMachine,
                      self.threeMachines[i].timeOnThirdMachine)
