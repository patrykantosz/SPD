import read
import factory


filename = input("Wpisz nazwe pliku: ")
x = read.Reader()
x.read(filename)

tab = []

y = factory.Factory()
y.set_order(x.cols, x.rows, x.taski)
