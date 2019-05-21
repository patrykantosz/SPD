import math

import makespan
import schrage


def find_by_id(carlier_object, id):
    index = 0
    for task in carlier_object.pi:
        if task.id == id:
            return index
        else:
            index += 1
    return -1

def do_carlier(carlier_object):
    carlier_object.U, carlier_object.pi = schrage.do_schrage(carlier_object.tasks)
    for i in carlier_object.pi:
        print("ID: ", i.id)

    if carlier_object.U < carlier_object.UB:
        carlier_object.UB = carlier_object.U
        carlier_object.opt_pi = carlier_object.pi

    #b index
    potential_b = []
    for j in range(0, len(carlier_object.tasks)):
        if makespan.makespan(carlier_object.pi) == (carlier_object.pi[j].times[2] + makespan.makespan_carlier(carlier_object.pi)[j]):
            potential_b.append(carlier_object.pi[j].id)
    carlier_object.b = max(potential_b)
    print("B: ", carlier_object.b)

    #a index
    potential_a = []
    for j in range(0, carlier_object.b + 1):
        sum_of = 0
        for i in range(j, carlier_object.b):
            sum_of += carlier_object.pi[i].times[1]
        if makespan.makespan(carlier_object.pi) == (sum_of + carlier_object.pi[j].times[0] + carlier_object.tasks[carlier_object.b].times[2]):
            potential_a.append(carlier_object.pi[j].id)
    carlier_object.a = min(potential_a)
    print("A: ", carlier_object.a)

    #c index
    potential_c = []
    index_a_in_pi = find_by_id(carlier_object, carlier_object.a)
    index_b_in_pi = find_by_id(carlier_object, carlier_object.b)
    for j in range(index_a_in_pi, index_b_in_pi + 1):
        if carlier_object.pi[j].times[2] < carlier_object.pi[carlier_object.b].times[2]:
            potential_c.append(j)
    print(max(potential_c))




