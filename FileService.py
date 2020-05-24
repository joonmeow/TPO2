import os


class FileService:
    def mergeTemporaryFiles(self, directory):
        self.directoryExist(directory)
        files = [os.path.join(directory, file) for file in os.listdir(directory)
                 if os.path.isfile(os.path.join(directory, file))]
        count = 0
        with open(os.path.join(directory, 'backup.tmp'), 'a') as backup:
            for file in files:
                text = self.backupFile(file)
                backup.write(text)
                count += 1
        return count

    def backupFile(self, file):
        with open(file) as f:
            text = f.read()
        os.remove(file)
        return text

    def directoryExist(self, directory):
        if os.path.isdir(directory) is False:
            raise ValueError


if __name__ == '__main__':
    fs = FileService()
    fs.mergeTemporaryFiles('D:\\')
