import task_class

def converter(list_of_tasks):
    index = 0
    converted_tasks = []
    for i in list_of_tasks:
        converted_tasks.append(task_class.Tasks(i, index))
        index += 1
    return converted_tasks
