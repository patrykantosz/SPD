import task_class
import math


class Schrage:
    def __init__(self, tasks):
        self.sigma = []
        self.sorted_tasks = []
        self.unsorted_tasks = self.convert_tasks(tasks)
        self.t = 0
        self.table_of_converted_tasks = self.convert_tasks(tasks)
        self.l = 0
        self.q = task_class.Tasks([0, 0, math.inf ],-1)
        self.c_max = 0

    def extract_r(self, tasks):
        r_list = []
        for task in tasks:
            r_list.append(task.times[0])
        return r_list

    def extract_q(self, tasks):
        q_list = []
        for task in tasks:
            q_list.append(task.times[2])
        return q_list

    def convert_tasks(self, tasks):
        list_of_tasks = []
        index = 0
        for task in tasks:
            list_of_tasks.append(task_class.Tasks(task, index))
            index += 1
        return list_of_tasks

    def do_schrage(self):
        j = None
        while self.sorted_tasks or self.unsorted_tasks:
            while self.unsorted_tasks and (min(self.extract_r(self.unsorted_tasks)) <= self.t):
                tmp_list = self.extract_r(self.unsorted_tasks)
                j = tmp_list.index(min(tmp_list))
                self.sorted_tasks.append(self.unsorted_tasks.pop(j))
            if not self.sorted_tasks:
                self.t = min(self.extract_r(self.unsorted_tasks))
            else:
                qs = self.extract_q(self.sorted_tasks)
                j = qs.index(max(qs))
                self.sigma.append(self.sorted_tasks.pop(j))
                self.t += self.sigma[-1].times[1]
        return self.sigma

    def do_schrage_pmtn(self):
        j = None
        while self.sorted_tasks or self.unsorted_tasks:
            while self.unsorted_tasks and (min(self.extract_r(self.unsorted_tasks)) <= self.t):
                tmp_list = self.extract_r(self.unsorted_tasks)
                j = tmp_list.index(min(tmp_list))
                self.sorted_tasks.append(self.unsorted_tasks.pop(j))
                if self.l == 0:
                    if self.sorted_tasks[-1].times[2] > self.q.times[2]:
                        self.l.times[1] = self.t - self.sorted_tasks[-1].times[0]
                        self.t = self.sorted_tasks[-1].times[0]
                        if self.l.times[1] > 0:
                            self.sorted_tasks.append(self.l)
                else:
                    if self.sorted_tasks[-1].times[2] > self.l.times[2]:
                        self.l.times[1] = self.t - self.sorted_tasks[-1].times[0]
                        self.t = self.sorted_tasks[-1].times[0]
                        if self.l.times[1] > 0:
                            self.sorted_tasks.append(self.l)

            if not self.sorted_tasks:
                self.t = min(self.extract_r(self.unsorted_tasks))
            else:
                qs = self.extract_q(self.sorted_tasks)
                j = qs.index(max(qs))
                self.l = self.sorted_tasks.pop(j)
                #print("L wynosi: ", self.l.id)
                self.t += self.l.times[1]
                self.c_max = max(self.c_max, self.t + self.l.times[2])
        return self.c_max

