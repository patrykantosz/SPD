from prettytable import PrettyTable as tabelki

import makespan
import read
import schrage
import converter

x = read.Reader()
x.read("data//in50.txt")
converted_tasks = converter.converter(x.my_data)


c_max, list = schrage.do_schrage(converted_tasks)
print(c_max)
c_max, list = schrage.do_schrage_pmtn(converted_tasks)
print(c_max)