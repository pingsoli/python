# Factory Pattern

class BaseArchive(object):
    EXTENSION = None

    def __init__(self, location_path, files_to_pack):
        self.location_path = location_path
        self.files_to_pack = files_to_pack

    def generate(self):
        raise NotImplementedError()

from zipfile import ZipFile
import tarfile

class ZipArchive(BaseArchive):
    EXTENSION = 'zip'

    def generate(self):
        with ZipFile('{}.{}'.format(
                        self.location_path, 
                        self.EXTENSION), 'w') as zip_file:
            for file_ in self.files_to_pack:
                zip_file.write(file_)

class TARArchive(BaseArchive):
    EXTENSION = 'tar'

    def generate(self):
        with tarfile.open('{}.{}'.format(
                            self.location_path,
                            self.EXTENSION), 'w') as tar_file:
            for file_ in self.files_to_pack:
                tar_file.add(file_)
