

class ReportViewer:
    def __init__(self, fileService, directory):
        self.fileService = fileService
        self.directory = directory
        self.removedFiles = 0

    def prepareData(self):
        removedFiles = self.fileService.mergeTemporaryFiles(self.directory)
        if removedFiles == 0:
            return
        self.removedFiles = removedFiles
