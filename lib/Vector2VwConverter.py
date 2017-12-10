import os
import json

from .helpers.TimeLogger import TimeLogger


class Vector2VwConverter:
    def __init__(self, input_file, output_file, number=0):
        self.tl = TimeLogger()
        self.input_file = input_file
        self.output_file = output_file
        self.number = number
        self.vector = self.read(input_file)

    @staticmethod
    def read(filename):
        with open(filename, 'r+') as vector_file_descriptor:
            return json.loads(vector_file_descriptor.read())

    @staticmethod
    def write(filename, content):
        with open(filename, 'a') as vw_file_descriptor:
            vw_file_descriptor.write(content)

    def print_stat(self):
        print('Vector (' + str(self.number) + ', ' + self.input_file + ') to Vowpal Wabbit transformation completed.'
                                                                       'Time: ' + str(self.tl.finish()))

    def convert(self):
        vw_line = ['%s |n' % self.number]

        for i, value in enumerate(self.vector):
            if float(value) == 0.0:
                continue
            vw_line.append('%s:%s' % (i + 1, value))

        self.write(self.output_file, ' '.join(vw_line) + os.linesep)
