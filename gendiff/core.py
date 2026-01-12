from gendiff.diff_builder import build_diff
from gendiff.formatter.stylish import format_stylish
from gendiff.parser import parse_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    else:
        print(f"Unknown format: {format_name}")

    '''result = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {str(data1[key]).lower()}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {str(data2[key]).lower()}")
        elif data1[key] != data2[key]:
            result.append(f"  - {key}: {str(data1[key]).lower()}")
            result.append(f"  + {key}: {str(data2[key]).lower()}")
        else:
            result.append(f"    {key}: {str(data1[key]).lower()}")



    result = "{\n" + "\n".join(result) + "\n}"
    
    return result'''


