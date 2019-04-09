from prettytable import PrettyTable

import factory
import annealing
import read
import os
import glob
from prettytable import PrettyTable
import numpy as np
import neh

# load all filenames
files = list(glob.glob(os.path.join("data", 'ta*')))

# tmp var for insert/swap test
annealing_c_max = 0
annealing_time = 0
summed_annealing_c_max = 0
summed_annealing_time = 0

annealing_c_max_insert = 0
annealing_time_insert = 0
summed_annealing_c_max_insert = 0
summed_annealing_time_insert = 0

# tmp var for cooling coefficient test
cooling_c_max = 0
cooling_time = 0
summed_cooling_c_max = 0
summed_cooling_time = 0

# tmp var for temperature test
temperature_c_max = 0
temperature_time = 0
summed_temperature_c_max = 0
summed_temperature_time = 0

# tmp var for probability test
probability_c_max = 0
probability_time = 0
probability_c_max_2 = 0
probability_time_2 = 0
summed_probability_c_max = 0
summed_probability_time = 0
summed_probability_c_max_2 = 0
summed_probability_time_2 = 0

# tmp var for neh test
neh_c_max = 0
neh_time = 0
not_neh_c_max = 0
not_neh_time = 0
summed_not_neh_c_max = 0
summed_not_neh_time = 0

# tmp var for neh's sequence test
neh_seq_c_max = 0
neh_seq_time = 0
summed_neh_seq_c_max = 0
summed_neh_seq_time = 0

# helpful vars
repeats = 3

x = read.Reader()
z = annealing.Annealing()
y = neh.Neh()

# cooling vars
list_of_u = [0.8, 0.9, 0.95, 0.99]

# temperature vars
start_temp = np.arange(200, 1200, 200)
stop_temp = np.arange(1,200,40)
stop_temp = stop_temp[::-1]

# table for swap/insert test
t = PrettyTable(['Tasks', 'Machines', 'Average C_Max for swap', 'Average C_Max for insert', 'Average Time for swap',
                 'Average Time for insert'])

# table for cooling coefficient test
t1 = PrettyTable(['Tasks', 'Machines', 'Cooling coefficient', 'Average C_Max', 'Average Time'])

# table for temperature test
t2 = PrettyTable(['Tasks', 'Machines', 'Initial temperature', 'End temperature', 'Average C_Max', 'Average Time'])

# table for probability test
t3 = PrettyTable(['Tasks', 'Machines', 'Average C_Max Normal Probability', 'Average C_Max Test Probabilty', 'Average Time Normal Probability', 'Average Time Test Probability'])

# table for neh test
t4 = PrettyTable(['Tasks', 'Machines', 'Neh C_max', 'Average C_Max', 'Neh Time', 'Average Time'])

# table for neh's sequence test
t5 = PrettyTable(['Tasks', 'Machines', 'Average C_Max', 'Average Time'])

# loop
for file in files:
    x.read(file)
    print("Read: ", file, ", tasks: ", x.rows, ", machines: ", x.cols)
    for i in range(repeats):
        # test of insert/swap loop
        annealing_c_max, annealing_time = z.simulated_annealing(x.my_data, x.cols, x.rows, "swap")
        annealing_c_max_insert, annealing_time_insert = z.simulated_annealing(x.my_data, x.cols, x.rows, "insert")
        summed_annealing_c_max += annealing_c_max
        summed_annealing_time += annealing_time
        summed_annealing_c_max_insert += annealing_c_max_insert
        summed_annealing_time_insert += annealing_time_insert
        # end of insert/swap loop

    print("Behind the first loop")

    # test of insert/swap section
    annealing_c_max = summed_annealing_c_max / repeats
    annealing_time = summed_annealing_time / repeats
    annealing_c_max_insert = summed_annealing_c_max_insert / repeats
    annealing_time_insert = summed_annealing_time_insert / repeats
    t.add_row([x.rows, x.cols, annealing_c_max, annealing_c_max_insert, annealing_time, annealing_time_insert])
    summed_annealing_c_max = 0
    summed_annealing_time = 0
    summed_annealing_c_max_insert = 0
    summed_annealing_time_insert = 0
    # end of insert/swap section

    # test of cooling coefficient section
    for u in list_of_u:
        for i in range(repeats):
            cooling_c_max, cooling_time = z.simulated_annealing(x.my_data, x.cols, x.rows, "swap", u)
            summed_cooling_c_max += cooling_c_max
            summed_cooling_time += cooling_time
            # test of cooling coefficient loop

        print("Behind the second loop")
        cooling_c_max = summed_cooling_c_max / repeats
        cooling_time = summed_cooling_time / repeats
        t1.add_row([x.rows, x.cols, u, cooling_c_max, cooling_time])
        cooling_c_max = 0
        cooling_time = 0
        summed_cooling_time = 0
        summed_cooling_c_max = 0
    # end of cooling coefficient section

    # test of temperature section
    for t_start in start_temp:
        for t_end in stop_temp:
            for i in range(repeats):
                temperature_c_max, temperature_time = z.simulated_annealing(x.my_data, x.cols, x.rows, "swap", 0.24, t_start,
                                                                    t_end)
                summed_temperature_c_max += temperature_c_max
                summed_temperature_time += temperature_time
            temperature_c_max = summed_temperature_c_max / repeats
            temperature_time = summed_temperature_time / repeats
            t2.add_row([x.rows, x.cols, t_start, t_end, temperature_c_max, temperature_time])
            temperature_time = 0
            temperature_c_max = 0
            summed_temperature_time = 0
            summed_temperature_c_max = 0
            print("Behind the third loop")
    #end of temperature section

    #test of probability section
    for i in range(repeats):
        probability_c_max, probability_time = z.simulated_annealing(x.my_data, x.cols, x.rows, "swap", 0.24, 2000, 1, 0)
        probability_c_max_2, probability_time_2 = z.simulated_annealing(x.my_data, x.cols, x.rows, "swap")
        summed_probability_c_max += probability_c_max
        summed_probability_time += probability_time
        summed_probability_c_max_2 += probability_c_max_2
        summed_probability_time_2 += probability_time_2
        print("Behind the fourth loop")
    probability_c_max = summed_probability_c_max/repeats
    probability_c_max_2 = summed_probability_c_max_2/repeats
    probability_time = summed_probability_time/repeats
    probability_time_2 = summed_probability_time_2/repeats
    t3.add_row([x.rows, x.cols, probability_c_max_2, probability_c_max, probability_time_2,  probability_time])
    probability_c_max = 0
    probability_c_max_2 = 0
    probability_time = 0
    probability_time_2 = 0
    summed_probability_c_max = 0
    summed_probability_c_max_2 = 0
    summed_probability_time = 0
    summed_probability_time_2 = 0
    #end of probability test section

    #neh test section
    for i in range(repeats):
        not_neh_c_max, not_neh_time = z.simulated_annealing(x.my_data, x.cols, x.rows, "swap")
        summed_not_neh_c_max += not_neh_c_max
        summed_not_neh_time += not_neh_time
        print("Behind the fifth loop")
    not_neh_c_max = summed_not_neh_c_max/repeats
    not_neh_time = summed_not_neh_time/repeats
    sequence, neh_c_max, neh_time = y.sum_times(x.my_data, x.cols, x.rows)
    t4.add_row([x.rows, x.cols, neh_c_max, not_neh_c_max, neh_time, not_neh_time])
    not_neh_c_max = 0
    not_neh_time = 0
    summed_not_neh_time = 0
    summed_not_neh_c_max = 0
    #end of neh test section
    print("Behind the last loop")

    #neh best sequence test section
    for i in range(repeats):
        neh_seq_c_max, neh_seq_time = z.simulated_annealing(x.my_data, x.cols, x.rows, "swap", 0.24, 2000, 1, 1, sequence)
        summed_neh_seq_c_max += neh_seq_c_max
        summed_neh_seq_time += neh_seq_time
    neh_seq_c_max = summed_neh_seq_c_max/repeats
    neh_seq_time = summed_neh_seq_time/repeats
    t5.add_row([x.rows, x.cols, neh_seq_c_max, neh_seq_time])
    neh_seq_c_max = 0
    neh_seq_time = 0
    summed_neh_seq_time = 0
    summed_neh_seq_c_max = 0

print(t)
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

data = t.get_string()
data1 = t1.get_string()
data2 = t2.get_string()
data3 = t3.get_string()
data4 = t4.get_string()
data5 = t5.get_string()

with open('tmp1.txt', 'w') as f:
    f.write("Tabel with results of swap/insert test")
    f.write(data)
    f.write("Tabel with results of cooling coefficient test")
    f.write(data1)
    f.write("Tabel with results of various temperature test")
    f.write(data2)
    f.write("Tabel with results of 2 methods of calculating probability test")
    f.write(data3)
    f.write("Tabel with results of comparing neh and annealing test")
    f.write(data4)
    f.write("Tabel with results of annealing algorithm with starting sequence from neh")
    f.write(data5)
