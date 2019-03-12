import read
import factory

filename = input("Wpisz nazwe pliku: ")
x = read.Reader()
read.Reader.read(x, filename)
print(x.counter)
print(x.machines)
print(x.rows)

factor = factory.Factory()
factor.startProduction(x)
factor.print()
