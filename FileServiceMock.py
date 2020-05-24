from ProdactionCode.IFilesService import IFileService


class FileServiceMock(IFileService):
    def __init__(self):
        self.countCall = 0

    def mergeTemporaryFiles(self, directory):
        self.countCall += 1
