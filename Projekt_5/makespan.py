def makespan(tasks):
    M = 0
    C_max = 0
    for task in tasks:
        M = max(M, task.times[0]) + task.times[1]
        C_max = max(C_max, M + task.times[2])
    return C_max

def makespan_carlier(tasks):
    M = 0
    C_max = 0
    C_max_list = []
    for task in tasks:
        M = max(M, task.times[0]) + task.times[1]
        C_max = max(C_max, M)
        C_max_list.append(C_max)
    return C_max_list
