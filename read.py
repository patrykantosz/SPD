import dataClass


class Reader:
    def __init__(self):
        self.counter = 0
        self.machines = 0
        self.rows = 0
        self.machinesInFactory = []

    def read(self, filename):
        with open(filename, "r") as f:
            while True:
                c = f.read(1)
                if not c:
                    print("End of file")
                    break
                if c.isdigit() is True:
                    if self.counter is 0:
                        self.rows = int(c)
                    elif self.counter is 1:
                        self.machines = int(c)
                    else:
                        self.machinesInFactory.append(int(c))
                    self.counter += 1
        print(len(self.machinesInFactory))


