


class FRIterator:
    def __init__(self, start, end, step=0.5):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        while self.start <= self.end:
            yield self.start
            self.start += self.step

    def __reversed__(self):
        while self.end >= self.start:
            yield self.end
            self.end -= self.step


fri = reversed(FRIterator(1, 5))
for x in fri:
    print(x)
