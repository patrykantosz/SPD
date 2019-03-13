class Reader:
    def __init__(self):
        self.cols = 0
        self.rows = 0
        self.my_data = []

    def read(self, filename):
        with open(filename, "r") as f:
            names_list = [l for l in (line.strip() for line in f) if l]
        # Extract dimensions from first line. Cast values to integers from strings.
        self.cols, self.rows = (int(val) for val in names_list[0].split())
        # Do a double-nested list comprehension to get the rest of the data into your matrix
        self.my_data = [[int(val) for val in line.split()] for line in names_list[1:]]
