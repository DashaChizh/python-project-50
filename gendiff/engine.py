import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
        )
    parser.add_argument(
        '-f', '--format',
        help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    parser.print_help

    data1 = json.load(open('file1.json'))
    data2 = json.load(open('file2.json'))
    print('file1: ', data1)
    print('file2: '/ data2)

    print(f"{args.first_file}, {args.second_file}")
    return args.first_file, args.second_file

