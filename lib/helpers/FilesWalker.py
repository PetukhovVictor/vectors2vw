from os import path
import glob


class FilesWalker:
    @staticmethod
    def walk(folder, callback, extension='json'):
        counter = 1
        for filename in glob.iglob(folder + '/**/*.' + extension, recursive=True):
            if path.isfile(filename):
                callback(filename, counter)
                counter += 1
