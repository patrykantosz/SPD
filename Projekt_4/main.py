import read
import schrage

x = read.Reader()
x.read("in50.txt")
y = schrage.Schrage(x.my_data)

tmp = []

x.read("in50.txt")
sigma = y.do_schrage()
for i in sigma:
    tmp.append(i.id)
print(tmp)
