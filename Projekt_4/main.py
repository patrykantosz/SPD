from prettytable import PrettyTable as tabelki

import makespan
import read
import schrage

x = read.Reader()
x.read("data//in50.txt")
y = schrage.Schrage(x.my_data)
y_1 = schrage.Schrage(x.my_data)

t = tabelki(['Alogrithm', 'in50', 'in100', 'in200', 'Sum'])

sigma = y.do_schrage()
c_max = makespan.makespan(sigma)
c_max_pmtn = y_1.do_schrage_pmtn()

x.read("data//in100.txt")
y_2 = schrage.Schrage(x.my_data)
y_3 = schrage.Schrage(x.my_data)

sigma = y_2.do_schrage()
c_max_1 = makespan.makespan(sigma)
c_max_pmtn_1 = y_3.do_schrage_pmtn()

x.read("data//in200.txt")
y_4 = schrage.Schrage(x.my_data)
y_5 = schrage.Schrage(x.my_data)

sigma = y_4.do_schrage()
c_max_2 = makespan.makespan(sigma)
c_max_pmtn_2 = y_5.do_schrage_pmtn()

t.add_row(['Schrage', c_max, c_max_1, c_max_2, c_max + c_max_1 + c_max_2])
t.add_row(['Schrage pmtn', c_max_pmtn, c_max_pmtn_1, c_max_pmtn_2, c_max_pmtn + c_max_pmtn_1 + c_max_pmtn_2])

print(t)
