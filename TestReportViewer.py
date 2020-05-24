import unittest
from ProdactionCode.ReportViewer import ReportViewer
from TestCode.Mock.FileServiceMock import FileServiceMock
from TestCode.Stub.FilesServiceStub import FileServiceStub, FileServiceStubValueError


class TestReportViewer(unittest.TestCase):
    def setUp(self):
        self.directory = 'D:\\TestDir'
        self.stubFileService = FileServiceStub().mergeTemporaryFiles(self.directory)

    def test_mock(self):
        fileService = FileServiceMock()
        reportViewer = ReportViewer(fileService, self.directory)
        reportViewer.prepareData()
        self.assertEqual(fileService.countCall, 1)

    def test_stub(self):
        fileService = FileServiceStub()
        reportViewer = ReportViewer(fileService, self.directory)
        reportViewer.prepareData()
        self.assertEqual(reportViewer.removedFiles, self.stubFileService)

    @unittest.expectedFailure
    def test_stub_value_error(self):
        fileService = FileServiceStubValueError()
        reportViewer = ReportViewer(fileService, self.directory)
        self.assertRaises(ValueError, reportViewer.prepareData())