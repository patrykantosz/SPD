import numpy


class Taski:
    def __init__(self, time, index):
        self.time = time
        self.id = index


class Factory:

    def makespan(self, sequence_order, times, number_of_machines):
        c_max = numpy.zeros((len(sequence_order) + 1, number_of_machines))
        for index in range(1, len(sequence_order)+1):
            c_max[index][0] = c_max[index-1][0] + times[sequence_order[index-1]][0]
        for index in range(1, number_of_machines):
            for index2 in range(1, len(sequence_order) + 1):
                c_max[index2][index] = max(c_max[index2][index-1], c_max[index2-1][index]) \
                                       + times[sequence_order[index2 - 1]][index]
        return c_max

    def permute(self, xs, low=0):
        if low + 1 >= len(xs):
            yield xs
        else:
            for p in self.permute(xs, low + 1):
                yield p
            for i in range(low + 1, len(xs)):
                xs[low], xs[i] = xs[i], xs[low]
                for p in self.permute(xs, low + 1):
                    yield p
                xs[low], xs[i] = xs[i], xs[low]

    def set_order(self, number_of_tasks, number_of_machines, tasks):
        number_order = []
        for i in range(number_of_tasks):
            number_order.append(i)
        for p in self.permute(number_order):
            print("Cmax for  permutation {} is equal {}".format(p, self.makespan(p, tasks, number_of_machines)[number_of_tasks][number_of_machines-1]))

    def johnson_for_two(self, tasks):
        first_half = []
        second_half = []
        object_tasks = []
        counter = 0
        for i in tasks:
            object_tasks.append(Taski(i, counter))
            counter += 1
        while len(object_tasks) > 0:
            index_to_order_1 = 0
            index_to_order_2 = 0
            for index in range(len(object_tasks)):
                if object_tasks[index].time[0] < object_tasks[index_to_order_1].time[0]:
                    index_to_order_1 = index
                if object_tasks[index].time[1] < object_tasks[index_to_order_2].time[1]:
                    index_to_order_2 = index

            if object_tasks[index_to_order_1].time[0] <= object_tasks[index_to_order_2].time[1]:
                first_half.append(object_tasks[index_to_order_1].id)
                del object_tasks[index_to_order_1]
            else:
                second_half.append(object_tasks[index_to_order_2].id)
                del object_tasks[index_to_order_2]

        return (first_half+second_half)

    def johnson_for_three(self, tasks, number_of_tasks):
        virtual_machine_1 = numpy.zeros((number_of_tasks, 2))
        for j in range(number_of_tasks):
            virtual_machine_1[j][0] = tasks[j][0] + tasks[j][1]
        for j in range(number_of_tasks):
            virtual_machine_1[j][1] = tasks[j][1] + tasks[j][2]
        task_order = self.johnson_for_two(virtual_machine_1)
        return task_order

    def johnson(self, tasks, number_of_machines, number_of_tasks):
        if number_of_machines == 2:
            number_order = self.johnson_for_two(tasks)
            print("Johnson permutation: {}, time for: {}".format(number_order,
                                                                 self.makespan(number_order, tasks, number_of_machines)[
                                                                     number_of_tasks][number_of_machines-1]))
        elif number_of_machines == 3:
            number_order = self.johnson_for_three(tasks, number_of_tasks)
            print("Johnson permutation: {}, time for: {}".format(number_order,
                                                                 self.makespan(number_order, tasks, number_of_machines)[
                                                                     number_of_tasks][number_of_machines - 1]))