import unittest
from unittest.mock import Mock
from ProdactionCode.IFilesService import IFileService
from ProdactionCode.ReportViewer import ReportViewer


class TestReportViewer(unittest.TestCase):
    def setUp(self):
        self.directory = 'D:\\TestDir'
        self.stubFileService = 3
        self.fileService = Mock(spec=IFileService)

    def test_mock(self):
        reportViewer = ReportViewer(self.fileService, self.directory)
        reportViewer.prepareData()
        self.fileService.mergeTemporaryFiles.assert_called_once()

    def test_stub(self):
        self.fileService.mergeTemporaryFiles.return_value = self.stubFileService
        reportViewer = ReportViewer(self.fileService, self.directory)
        reportViewer.prepareData()
        self.assertEqual(reportViewer.removedFiles, self.stubFileService)

    @unittest.expectedFailure
    def test_stub_value_error(self):
        self.fileService.mergeTemporaryFiles.side_effect = ValueError
        reportViewer = ReportViewer(self.fileService, self.directory)
        self.assertRaises(ValueError, reportViewer.prepareData())
