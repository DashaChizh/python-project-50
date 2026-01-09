import json


def compare_datas(data1, data2):
    result = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    
        
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in data1 and key not in data2:
            result.append(f"  - {key}: {format_value(value1)}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {format_value(value2)}")
        elif value1 == value2:
            result.append(f"    {key}: {format_value(value1)}")
        else:
            result.append(f"  - {key}: {format_value(value1)}")
            result.append(f"  + {key}: {format_value(value2)}")

    return result
    
def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)    

def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = json.load(open(filepath1))
    data2 = json.load(open(filepath2))

    diff_lines = compare_datas(data1, data2)

    result = "{\n" + "\n".join(diff_lines) + "\n}"
    
    return result


