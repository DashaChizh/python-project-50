def format_stylish(diff, depth=0):
    lines = []
    indent_size = 4
    current_indent = ' ' * (depth * indent_size)
   
    for node in diff:
        key = node['key']
        node_type = node['type']
       
        if node_type == 'nested':
            children_str = format_stylish(node['children'], depth + 1)
            lines.append(f"{current_indent}    {key}: {children_str}")
       
        elif node_type == 'unchanged':
            value_str = format_value(node['value'], depth + 1)
            lines.append(f"{current_indent}    {key}: {value_str}")
       
        elif node_type == 'added':
            value_str = format_value(node['value'], depth + 1)
            lines.append(f"{current_indent}  + {key}: {value_str}")
       
        elif node_type == 'removed':
            value_str = format_value(node['value'], depth + 1)
            lines.append(f"{current_indent}  - {key}: {value_str}")
       
        elif node_type == 'changed':
            value1_str = format_value(node['value1'], depth + 1)
            value2_str = format_value(node['value2'], depth + 1)
            lines.append(f"{current_indent}  - {key}: {value1_str}")
            lines.append(f"{current_indent}  + {key}: {value2_str}")
   
    result = "{\n" + "\n".join(lines) + "\n" + current_indent + "}"
    return result


def format_value(value, depth):
    if isinstance(value, dict):
        return format_dict(value, depth)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def format_dict(data, depth):
    if not data:
        return '{}'
   
    lines = []
    indent_size = 4
    current_indent = ' ' * (depth * indent_size)
   
    for key, value in sorted(data.items()):
        value_str = format_value(value, depth + 1)
        lines.append(f"{current_indent}    {key}: {value_str}")
   
    return "{\n" + "\n".join(lines) + "\n" + current_indent + "}"