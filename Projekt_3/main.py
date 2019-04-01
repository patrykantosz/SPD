from prettytable import PrettyTable

import factory
import neh
import read

x = read.Reader()
y = neh.Neh()
z = factory.Factory()

neh_sequence = []
neh_c_max = 0
neh_time = 0
johnson_sequence = []
johnson_c_max = 0
johnson_time = 0

list_of_files = ["ta000.txt", "ta001.txt", "ta002.txt", "ta004.txt", "ta003.txt"]

t = PrettyTable(['NEH C_max', 'Johnsons C_max', 'NEH Time', 'Johnsons Time'])
for file in list_of_files:
    x.read(file)
    neh_sequence, neh_c_max, neh_time = y.sum_times(x.my_data, x.cols, x.rows)
    johnson_sequence, johnson_c_max, johnson_time = z.johnson(x.my_data, x.cols, x.rows)
    t.add_row([neh_c_max, johnson_c_max, neh_time, johnson_time])
print(t)





