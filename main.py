import argparse

from lib.helpers.FilesWalker import FilesWalker
from lib.Vector2VwConverter import Vector2VwConverter


parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', '-i', nargs=1, type=str, help='folder with feature vectors')
parser.add_argument('--output_file', '-o', nargs=1, type=str, help='Output Vowpal Wabbit file')
args = parser.parse_args()

input_folder = args.input_folder[0]
output_file = args.output_file[0]


def vectors_process(filename, counter):
    v2vw = Vector2VwConverter(filename, output_file, counter)
    v2vw.convert()
    v2vw.print_stat()


FilesWalker.walk(input_folder, vectors_process)
