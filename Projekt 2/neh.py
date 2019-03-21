class Taski:
    def __init__(self, time, id):
        self.time = time
        self.id = id
    def __lt__(self, other):
        return self.time < other.time

class Neh:
    def __init__(self):
        self.sumed = []

    def sum_times(self, tasks, number_of_tasks):
        counter = 0
        for t in tasks:
            if counter <= number_of_tasks:
                self.sumed.append(Taski(sum(t), counter))
                counter += 1
        self.sumed.sort()