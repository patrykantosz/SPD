import dataClass


class Reader:
    def __init__(self):
        self.counter = 0
        self.machines = 0
        self.rows = 0

    def read(self, filename):
        with open(filename, "r") as f:
            while True:
                c = f.read(1)
                if not c:
                    print("End of file")
                    break
                if c.isdigit():
                    if self.counter is 0:
                        self.rows = c
                        print(self.rows + " " + c)
                    elif self.counter is 1:
                        self.machines = c
                        print(self.machines + " " + c)
                print(self.counter)
                self.counter += 1
