def build_diff(data1, data2):
    diff = []

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        if key in data1 and key not in data2:
            diff.append({
                'key': key,
                'type': 'removed',
                'value': data1[key]
            })

        elif key not in data1 and key in data2:
            diff.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })

        elif key in data1 and key in data2:
            value1 = data1[key]
            value2 = data2[key]

            if isinstance(value1, dict) and isinstance(value2, dict):
                children = build_diff(value1, value2)
                diff.append({
                    'key': key,
                    'type': 'nested',
                    'children': children
                })

            elif value1 != value2:
                diff.append({
                    'key': key,
                    'type': 'changed',
                    'value1': value1,
                    'value2': value2
                })

            else:
                diff.append({
                    'key': key,
                    'type': 'unchanged',
                    'value': value1
                })

    return diff
            

        
