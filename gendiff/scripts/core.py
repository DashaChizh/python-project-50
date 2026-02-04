from gendiff.scripts.diff_builder import build_diff
from gendiff.formatter import get_formatter
from gendiff.scripts.parser import parse_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)

    formatter = get_formatter(format_name)
    return formatter(diff)