import read
import schrage

x = read.Reader()
x.read("in50.txt")
y = schrage.Schrage(x.my_data)

tmp = [[1, 2, 3], [5, 432, 567], [1, 3, 5]]

x.read("in50.txt")
sigma = y.do_schrage()
