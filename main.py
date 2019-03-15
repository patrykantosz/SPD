import read
import factory


filename = input("Enter the filename: ")
x = read.Reader()
x.read(filename)

tab = []

y = factory.Factory()
y.set_order(x.cols, x.rows, x.my_data)
y.johnson(x.my_data, x.rows, x.cols)
