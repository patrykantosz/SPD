import glob
import os

from prettytable import PrettyTable as tabel

import carlier
import carlier_task
import converter
import read

# load files
files = list(glob.glob(os.path.join("data", '*')))

correct_times = [228, 3026, 3665, 3309, 3191, 3618, 3446, 3821, 3634, 3070, 6398, 1492]
t = tabel(['File name', 'Correct time', 'Calculated time', 'Is calculated time correct?'])
index = 0
correct = 0
x = read.Reader()

for file in files:
    x.read(file)
    converted_tasks = converter.converter(x.my_data)
    carlier_object = carlier_task.Carlier_Task(converted_tasks)
    c_max = carlier.do_carlier(carlier_object)
    t.add_row([file[5:], correct_times[index], c_max, correct_times[index] == c_max])
    if correct_times[index] == c_max:
        correct += 1
    index += 1
string = str(str(correct) + "/" + str(index))
print(string)
t.add_row(["", "", "", ""])
t.add_row(["", "", "Passed: ", string])

print(t)
