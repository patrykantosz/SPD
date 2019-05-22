import copy

import makespan
import schrage


def calc_k(carlier_object, K_):
    # r_(K), q_(K), p_(K)
    potential_r_k_ = []
    potential_p_k_ = []
    potential_q_k_ = []
    for j in K_:
        potential_r_k_.append(carlier_object.pi[j].times[0])
        potential_p_k_.append(carlier_object.pi[j].times[1])
        potential_q_k_.append(carlier_object.pi[j].times[2])
    r_k_ = min(potential_r_k_)
    p_k_ = sum(potential_p_k_)
    q_k_ = min(potential_q_k_)

    # h(K u {c})
    h_k_ = r_k_ + p_k_ + q_k_

    return h_k_, r_k_, p_k_, q_k_


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

    if carlier_object.U < carlier_object.UB:
        carlier_object.UB = copy.deepcopy(carlier_object.U)
        carlier_object.opt_pi = copy.deepcopy(carlier_object.pi)

    # b index
    potential_b = []
    for j in range(0, len(carlier_object.tasks)):
        if makespan.makespan(carlier_object.pi) == (
                carlier_object.pi[j].times[2] + makespan.makespan_carlier(carlier_object.pi)[j]):
            potential_b.append(carlier_object.pi[j].id)
    carlier_object.b = max(potential_b)

    # a index
    for j in range(0, len(carlier_object.tasks)):
        sum_of = 0
        for i in range(j, find_by_id(carlier_object, carlier_object.b) + 1):
            sum_of += carlier_object.pi[i].times[1]
        if carlier_object.U == (
                sum_of + carlier_object.pi[j].times[0] + carlier_object.tasks[carlier_object.b].times[2]):
            carlier_object.a = carlier_object.pi[j].id
            break
    carlier_object.a = find_by_id(carlier_object, carlier_object.a)
    carlier_object.b = find_by_id(carlier_object, carlier_object.b)

    # c index
    potential_c = []
    for j in range(carlier_object.a, carlier_object.b + 1):
        if carlier_object.pi[j].times[2] < carlier_object.pi[carlier_object.b].times[2]:
            potential_c.append(j)
    if potential_c:
        carlier_object.c = max(potential_c)
    else:
        return carlier_object.U

    # K block
    K = []  # K to blok, w którym są indeksy do pi[index]
    for j in range(carlier_object.c + 1, carlier_object.b + 1):
        K.append(j)

    # K u {c} block
    K_ = []  # K to blok, w którym są indeksy do pi[index]
    for j in range(carlier_object.c, carlier_object.b + 1):
        K_.append(j)

    # r(K), q(K), p(K), h(K)
    h_k, r_k, p_k, q_k = calc_k(carlier_object, K)

    # remember tasks[c].times[0]
    old_r_pi = copy.deepcopy(carlier_object.tasks[carlier_object.pi[carlier_object.c].id].times[0])

    # new tasks[c].times[0]
    carlier_object.tasks[carlier_object.pi[carlier_object.c].id].times[0] = max(
        carlier_object.tasks[carlier_object.pi[carlier_object.c].id].times[0], r_k + p_k)
    carlier_object.LB = schrage.do_schrage_pmtn(carlier_object.tasks)[0]

    h_k_c, r_k_c, p_k_c, q_k_c = calc_k(carlier_object, K_)
    carlier_object.LB = max(h_k, h_k_c, carlier_object.LB)

    # left if
    if carlier_object.LB < carlier_object.UB:
        do_carlier(carlier_object)

    # restore tasks[c].times[0]
    carlier_object.tasks[carlier_object.pi[carlier_object.c].id].times[0] = old_r_pi

    # remember tasks[c].times[2]
    old_q_pi = copy.deepcopy(carlier_object.pi[carlier_object.c].times[2])

    carlier_object.tasks[carlier_object.pi[carlier_object.c].id].times[2] = max(
        carlier_object.tasks[carlier_object.pi[carlier_object.c].id].times[2],
        q_k + p_k)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    carlier_object.LB = schrage.do_schrage_pmtn(carlier_object.tasks)[0]

    h_k_c, r_k_c, p_k_c, q_k_c = calc_k(carlier_object, K_)
    carlier_object.LB = max(h_k, h_k_c, carlier_object.LB)

    if carlier_object.LB < carlier_object.UB:
        do_carlier(carlier_object)
    carlier_object.tasks[carlier_object.pi[carlier_object.c].id].times[2] = old_q_pi

    return carlier_object.U
