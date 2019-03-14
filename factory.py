class Factory:
    def __init__(self):
        self.k =0


    # def calculate_time(self, number_of_tasks, number_of_machines, tasks):
    #     time = tasks[0].times[0]
    #     time1 = time
    #     print("Time: ", time, ", Time1: ", time1)
    #     counter = 1
    #     for t in tasks:
    #         print(t.times)
    #     time += max(tasks[0].times[1], tasks[1].times[0])
    #     print("Time: ", time)
    #     if (tasks[1].times[1] > tasks[2].times[0]):
    #         time += max(tasks[1].times[1], tasks[2].times[0])
    #     else:
    #
    #     print("Wartość 1:", tasks[1].times[1], "Wartość 2: ", tasks[2].times[0])
    #     print("Time: ", time)
    #     time += max(tasks[2].times[1], tasks[3].times[0])
    #     print("Time: ", time)
    #     time += tasks[3].times[1]
    #     print("Time: ", time)
    #     for i in range(number_of_tasks-1):
    #         time1 += max(tasks[i].times[number_of_machines-1], tasks[counter].times[0])
    #         counter += 1
    #     time1 += tasks[number_of_tasks-1].times[number_of_machines-1]
    #     print( "Time: ", time, ", Time1: ", time1)


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
        task_order = []
        counter = 1
        for i in tasks:
            number_order.append(i.number) #set list with numerical order
        for p in self.permute(number_order):
            print("Po prostu: ", p, " Coun: ", counter)
            counter += 1
            for j in p:
                for task in tasks:
                    if task.number == j:
                        task_order.append(task) #set list of order with task objects
                        print("Kaka ", task.times)
        print(task_order)
        print(len(task_order))
        #self.calculate_time(number_of_tasks, number_of_machines, task_order)



