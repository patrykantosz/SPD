class Reader:

    def __init__(self):
        self.cols = 0
        self.rows = 0
        self.my_data = []

    def read(self, filename):
        with open(filename, "r") as f:
            names_list = [l for l in (line.strip() for line in f) if l]
        self.cols, self.rows = (int(val) for val in names_list[0].split())
        self.my_data = [[int(val) for val in line.split()] for line in names_list[1:]]
        print(self.my_data)
