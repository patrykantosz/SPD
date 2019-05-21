import math

import makespan
import schrage


def do_carlier(tasks, carlier_object):
    carlier_object.U, carlier_object.pi = schrage.do_schrage(tasks)

    if carlier_object.U < carlier_object.UB:
        carlier_object.UB = carlier_object.U
        carlier_object.opt_pi = carlier_object.pi

    #b index
    potential_b = []
    for j in range(0, len(tasks)):
        if makespan.makespan(carlier_object.pi) == (carlier_object.pi[j].times[2] + makespan.makespan_carlier(carlier_object.pi)[j]):
            potential_b.append(carlier_object.pi[j].id)
    carlier_object.b = max(potential_b)
    print(carlier_object.b)

    #a index
    potential_a = []
    for j in range(0, carlier_object.b + 1):
        sum_of = 0
        for i in range(0, carlier_object.b + 1):
            sum_of += carlier_object.pi[i].times[1]
        print(j, sum_of, carlier_object.pi[j].times[0], carlier_object.pi[carlier_object.b].times[2], sum_of + carlier_object.pi[carlier_object.b].times[2] + carlier_object.pi[j].times[0])
        if makespan.makespan(carlier_object.pi) == (sum_of + carlier_object.pi[j].times[0] + carlier_object.pi[carlier_object.b].times[2]):
            print("Tu")


