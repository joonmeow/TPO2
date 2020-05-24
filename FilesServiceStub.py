from ProdactionCode.IFilesService import IFileService


class FileServiceStubValueError(IFileService):
    def mergeTemporaryFiles(self, directory):
        raise ValueError


class FileServiceStub(IFileService):
    def mergeTemporaryFiles(self, directory):
        return 3
