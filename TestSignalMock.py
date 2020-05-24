import unittest, os
from unittest.mock import Mock
from ProdactionCode.Signal import Signal
from ProdactionCode.IArrayProcessor import IArrayProcessor


class TestSignal(unittest.TestCase):
    def setUp(self):
        self.inputArray = [-12, -23, 0, -4, 2, 55, -23, -4, 55, 2, 3, 2, 12]
        self.samples = [55, 23, 12, 4, 3, 2, 0]
        self.fileResults = 'results.log'
        self.textResult = ['Сумма: 99\n', 'Разница: 11\n', 'Среднее: 14']

    def tearDown(self):
        if os.path.exists(os.path.join(os.getcwd(), self.fileResults)):
            os.remove(os.path.join(os.getcwd(), self.fileResults))

    def test_mock(self):
        arrayProcessor = Mock(spec=IArrayProcessor)
        arrayProcessor.sortAndFilter.return_value = self.samples
        signal = Signal(arrayProcessor)
        signal.inputArray = self.inputArray
        signal.fullRectify()
        arrayProcessor.sortAndFilter.assert_called_once()

    def test_stub(self):
        arrayProcessor = Mock(spec=IArrayProcessor)
        arrayProcessor.sortAndFilter.return_value = self.samples
        signal = Signal(arrayProcessor)
        signal.inputArray = self.inputArray
        signal.fullRectify()
        samplesTrue = True if signal.samples == self.samples else False
        resultFileExist = True if os.path.exists(os.path.join(os.getcwd(), self.fileResults)) else False
        with open(os.path.join(os.getcwd(), self.fileResults), 'r') as result:
            textResultFile = result.readlines()
        textFileTrue = True if textResultFile == self.textResult else False
        fileTrue = True if resultFileExist and textFileTrue else False
        self.assertEqual(True, fileTrue, samplesTrue)

    def test_if_result_exist(self):
        open(os.path.join(os.getcwd(), self.fileResults), 'a').close()
        self.fileResults = 'results(1).log'
        try:
            self.test_stub()
        finally:
            os.remove(os.path.join(os.getcwd(), 'results.log'))
