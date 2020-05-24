import os
from ProdactionCode.ArrayProcessor import ArrayProcessor


class Signal:
    def __init__(self, arrayProcessor):
        self.samples = []
        self.inputArray = []
        self.arrayProcessor = arrayProcessor
        self.filename = 'results'

    def fullRectify(self):
        self.samples = self.arrayProcessor.sortAndFilter(self.inputArray)
        results = self.calculateResults()
        filename = self.createFile(self.filename)
        with open(filename, 'w') as file:
            file.writelines(results)

    def createFile(self, filename, additional=0):
        addName = '' if additional == 0 else '(%s)' % additional
        uniqueFilename = filename + addName + '.log'
        directory = os.getcwd()
        if os.path.exists(os.path.join(directory, uniqueFilename)):
            uniqueFilename = self.createFile(filename, additional + 1)
        else:
            open(os.path.join(directory, uniqueFilename), 'a').close()
        return os.path.join(directory, uniqueFilename)

    def calculateResults(self):
        summary = 0
        for x in self.samples:
            summary += x
        average = summary // len(self.samples)
        difference = self.samples[0] * 2 - summary
        results = ['Сумма: ' + str(summary) + '\n', 'Разница: ' + str(difference) + '\n', 'Среднее: ' + str(average)]
        return results
