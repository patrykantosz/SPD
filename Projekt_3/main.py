from prettytable import PrettyTable

import factory
import annealing
import read

x = read.Reader()
x.read("ta001.txt")
z = annealing.Annealing()
z.simulated_annealing(x.my_data, x.cols, x.rows)










