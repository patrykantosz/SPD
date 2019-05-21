from prettytable import PrettyTable as tabelki

import carlier_task
import makespan
import read
import schrage
import converter
import carlier

x = read.Reader()
x.read("data//in50.txt")
converted_tasks = converter.converter(x.my_data)
carlier_object = carlier_task.Carlier_Task(converted_tasks)


c_max, list = schrage.do_schrage(converted_tasks)
print(c_max)
c_max, list = schrage.do_schrage_pmtn(converted_tasks)
print(c_max)
carlier.do_carlier(carlier_object)