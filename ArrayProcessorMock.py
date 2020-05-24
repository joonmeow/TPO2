from ProdactionCode.IArrayProcessor import IArrayProcessor


class ArrayProcessorMock(IArrayProcessor):
    def __init__(self):
        self.countCall = 0

    def sortAndFilter(self, a):
        self.countCall += 1
        return [55, 23, 12, 4, 3, 2, 0]
