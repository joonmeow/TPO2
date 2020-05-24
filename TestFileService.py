import unittest, os, shutil
from ProdactionCode.FileService import FileService


class TestFileService(unittest.TestCase):
    def setUp(self):
        self.fileService = FileService()
        self.pathDirectory = 'D:\\TestDir'
        self.pathEmptyDirectory = 'D:\\EmptyTestDir'
        self.pathFalseDirectory = 'D:\\Con'
        self.files = ['test.txt', 'test.bat', 'test.asm']
        self.fileBackup = 'backup.tmp'
        self.textBackup = 'text: test.asmtext: test.battext: test.txt'
        os.mkdir(self.pathDirectory)
        os.mkdir(self.pathEmptyDirectory)
        for file in self.files:
            with open(os.path.join(self.pathDirectory, file), 'a') as f:
                f.write('text: ' + file)

    def tearDown(self):
        shutil.rmtree(self.pathDirectory)
        shutil.rmtree(self.pathEmptyDirectory)

    def test_backup_files(self):
        count = self.fileService.mergeTemporaryFiles(self.pathDirectory)
        trueCount = True if count == len(self.files) else False
        filesCount = True if len(os.listdir(self.pathDirectory)) == 1 else False
        fileBackupExist = True if os.path.isfile(os.path.join(self.pathDirectory, self.fileBackup)) else False
        with open(os.path.join(self.pathDirectory, self.fileBackup), 'r') as f:
            linesBackup = f.read()
        textBackupConsist = True if linesBackup == self.textBackup else False
        isBackup = True if filesCount is fileBackupExist is textBackupConsist else False
        self.assertEqual(True, trueCount, isBackup)

    def test_empty_dir_backup_files(self):
        countFiles = len(os.listdir(self.pathEmptyDirectory))
        count = self.fileService.mergeTemporaryFiles(self.pathEmptyDirectory)
        trueCount = True if count == countFiles else False
        filesCount = True if len(os.listdir(self.pathEmptyDirectory)) == 1 else False
        fileBackupExist = True if os.path.isfile(os.path.join(self.pathEmptyDirectory, self.fileBackup)) else False
        with open(os.path.join(self.pathEmptyDirectory, self.fileBackup), 'r') as f:
            linesBackup = f.read()
        textBackupConsist = True if linesBackup == '' else False
        isBackup = True if filesCount is fileBackupExist is textBackupConsist else False
        self.assertEqual(True, trueCount, isBackup)

    @unittest.expectedFailure
    def test_no_directory(self):
        self.assertRaises(ValueError, self.fileService.mergeTemporaryFiles(self.pathFalseDirectory))
