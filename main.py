import read
import factory

filename = input("Wpisz nazwe pliku: ")
x = read.Reader()
x.read(filename)

y = factory.Factory()

for h in x.my_data:
    for p in y.permute(h):
        print(p)
