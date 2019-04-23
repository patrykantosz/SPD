import task_class


class Schrage:
    def __init__(self, tasks):
        self.i = 0
        self.sigma = []
        self.sorted_tasks = []
        self.unsorted_tasks = self.convert_tasks(tasks)
        self.t = min(self.extract_r(self.convert_tasks(tasks)))
        self.table_of_converted_tasks = self.convert_tasks(tasks)

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
        while self.sorted_tasks or self.unsorted_task:
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
                self.i += 1
                self.t += self.table_of_converted_tasks[j].times[1]
        return self.sigma
