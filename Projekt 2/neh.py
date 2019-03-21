import numpy

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
        for index in range(1, len(sequence_order)+1):
            c_max[index][0] = c_max[index-1][0] + times[sequence_order[index-1]][0]
        for index in range(1, number_of_machines):
            for index2 in range(1, len(sequence_order) + 1):
                c_max[index2][index] = max(c_max[index2][index-1], c_max[index2-1][index]) \
                                       + times[sequence_order[index2 - 1]][index]
        return c_max

    def sequence_maker(self, task_number, prev_seq):
        seq = []
        for i in range(len(prev_seq)+1):
            new_seq = prev_seq[:]
            new_seq.insert(i, task_number)
            seq.append(new_seq)
        return seq


    def neh_algorithm(self, tasks, number_of_machines):
        final_order = []
        # for i in self.first_order:
        #     shortest_time = float("10000000.00")
        #     best_time_seq = []
        #     seq = self.sequence_maker(i, final_order)
        #
        #     for s in seq:
        #         if self.makespan(s, tasks, number_of_machines) < shortest_time:
        #             shortest_time = self.makespan(s, tasks, number_of_machines)
        #             best_time_seq = seq
        #     final_order = best_time_seq
        #
        # return final_order





    def sum_times(self, tasks, number_of_machines):
        counter = 0
        print(number_of_machines)
        for t in tasks:
            if counter <= number_of_machines:
                self.sumed.append(Taski(sum(t), counter))

                counter += 1
        self.sumed.sort(reverse=True)
        for i in self.sumed:
            self.first_order.append(i.id)
        print(min(self.sumed).id)
        print(self.first_order)
        # print(self.neh_algorithm(tasks, number_of_machines))
