def format_value(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return str(value)


def format_plain(diff, current_path=''):
    lines = []
    
    for node in diff:
        key = node['key']
        node_type = node['type']
        
        full_path = f"{current_path}.{key}" if current_path else key
        
        if node_type == 'nested':
            children_result = format_plain(node['children'], full_path)
            if children_result:
                lines.append(children_result)
        
        elif node_type == 'added':
            value = format_value(node['value'])
            lines.append(
                f"Property '{full_path}' was added with value: {value}"
                )
        
        elif node_type == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        
        elif node_type == 'changed':
            old_val = format_value(node['value1'])
            new_val = format_value(node['value2'])
            lines.append(
                f"Property '{full_path}' was updated. "
                f"From {old_val} to {new_val}"
                )
    
    return '\n'.join(lines)