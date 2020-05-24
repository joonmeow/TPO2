import numpy


class ArrayProcessor:
    def sortAndFilter(self, a):
        array = [numpy.abs(x) for x in a]
        array = list(set(array))
        array.sort(reverse=True)
        return array
