import copy
import math

import numpy

import makespan
import task_class


def extract_column(tasks, column_number):
    r_list = []
    for task in tasks:
        r_list.append(task.times[column_number])
    return r_list


def do_schrage(tasks):
    ready_tasks = []
    final_list = []
    unready_tasks = copy.deepcopy(tasks)
    t = min(extract_column(unready_tasks, 0))

    while ready_tasks or unready_tasks:
        while unready_tasks and min(extract_column(unready_tasks, 0)) <= t:
            j = numpy.argmin(extract_column(unready_tasks, 0))
            ready_tasks.append(unready_tasks.pop(j))
        if not ready_tasks:
            t = min(extract_column(unready_tasks, 0))
        else:
            j = numpy.argmax(extract_column(ready_tasks, 2))
            final_list.append(ready_tasks.pop(j))
            t += final_list[-1].times[1]
    return makespan.makespan(final_list), final_list


def do_schrage_pmtn(tasks):
    ready_tasks = []
    final_list = []
    unready_tasks = copy.deepcopy(tasks)
    t = 0
    c_max = 0
    q_l = math.inf
    task_l = task_class.Tasks([0, 0, q_l], -1)

    while ready_tasks or unready_tasks:
        while unready_tasks and min(extract_column(unready_tasks, 0)) <= t:
            j = numpy.argmin(extract_column(unready_tasks, 0))
            ready_tasks.append(unready_tasks.pop(j))
            if ready_tasks[-1].times[2] > task_l.times[2]:
                task_l.times[1] = t - ready_tasks[-1].times[0]
                t = ready_tasks[-1].times[0]
                if task_l.times[1] > 0:
                    ready_tasks.append(task_l)
        if not ready_tasks:
            t = min(extract_column(unready_tasks, 0))
        else:
            j = numpy.argmax(extract_column(ready_tasks, 2))
            task_l = ready_tasks.pop(j)
            t += task_l.times[1]
            c_max = max(c_max, t + task_l.times[2])
            final_list.append(task_l)
    return c_max, final_list
