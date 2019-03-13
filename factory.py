class Factory:
    def __init__(self):
        self.k =0

    def permute(self, xs, low=0):
        if low + 1 >= len(xs):
            yield xs
        else:
            for p in self.permute(xs, low + 1):
                yield p
            for i in range(low + 1, len(xs)):
                xs[low], xs[i] = xs[i], xs[low]
                for p in self.permute(xs, low + 1):
                    yield p
                xs[low], xs[i] = xs[i], xs[low]