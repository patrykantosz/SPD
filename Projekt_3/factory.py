import numpy
import time


class Taski:
    def __init__(self, time, id):
        self.time = time
        self.id = id

    def __lt__(self, other):
        return self.time < other.time


class Neh:
    def __init__(self):
        self.sumed = []
        self.first_order = []

    def makespan(self, sequence_order, times, number_of_machines):
        c_max = numpy.zeros((len(sequence_order) + 1, number_of_machines))
        for index in range(1, len(sequence_order) + 1):
            c_max[index][0] = c_max[index - 1][0] + times[sequence_order[index - 1]][0]
        for index in range(1, number_of_machines):
            for index2 in range(1, len(sequence_order) + 1):
                c_max[index2][index] = max(c_max[index2][index - 1], c_max[index2 - 1][index]) \
                                       + times[sequence_order[index2 - 1]][index]
        return c_max[-1][-1]  # return only last element in array

    def sequence_maker(self, task_number, prev_seq):
        seq = []
        for i in range(len(prev_seq) + 1):
            new_seq = prev_seq[:]
            new_seq.insert(i, task_number)
            seq.append(new_seq)
        return seq