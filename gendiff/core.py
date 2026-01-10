import json

import yaml


def load_data(filepath):
    if filepath.endswith('.json'):
        return json.load(open(filepath))
    if filepath.endswith(('.yaml', '.yml')):
        return yaml.safe_load(open(filepath))


def generate_diff(filepath1, filepath2):
    data1 = load_data(filepath1)
    data2 = load_data(filepath2)

    result = []
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

    # diff_lines = compare_datas(data1, data2)
    # result = "{\n" + "\n".join(diff_lines) + "\n}"

    result = "{\n" + "\n".join(result) + "\n}"
    
    return result


