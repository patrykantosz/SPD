import read
import neh

x = read.Reader()
y = neh.Neh()

x.read("ta000.txt")

y.sum_times(x.my_data, x.cols, x.rows)

for t in y.sumed:
    print("Id: ", t.id, ", time: ", t.time)
