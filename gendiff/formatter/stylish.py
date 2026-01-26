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


'''INDENT_SIZE = 4


def format_stylish(diff, depth=0):  

    def format_value(value, current_depth):
        if isinstance(value, dict):
            if not value:
                return '{}'
            
            current_indent = ' ' * (current_depth * INDENT_SIZE)
            inner_lines = []
            
            for dict_key, dict_value in sorted(value.items()):
                formatted_value = format_value(dict_value, current_depth + 1)
                inner_lines.append(
                    f"{current_indent}    {dict_key}: {formatted_value}"
                )
            return "{\n" + "\n".join(inner_lines) + "\n" + current_indent + "}"
        
        if value is None:
            return 'null'
        if isinstance(value, bool):
            return 'true' if value else 'false'
        return str(value)
    
    current_indent = ' ' * (depth * INDENT_SIZE)
    result_lines = []
    
    for node in diff:
        node_key = node['key']
        node_type = node['type']
        
        match node_type:
            case 'nested':
                children_formatted = format_stylish(node['children'], depth + 1)
                result_lines.append(
                    f"{current_indent}    {node_key}: {children_formatted}"
                    )
        
            case 'unchanged':
                formatted_value = format_value(node['value'], depth + 1)
                result_lines.append(
                    f"{current_indent}    {node_key}: {formatted_value}"
                    )
        
            case 'added':
                formatted_value = format_value(node['value'], depth + 1)
                result_lines.append(
                    f"{current_indent}  + {node_key}: {formatted_value}"
                    )
        
            case 'removed':
                formatted_value = format_value(node['value'], depth + 1)
                result_lines.append(
                    f"{current_indent}  - {node_key}: {formatted_value}"
                    )
        
            case 'changed':
                old_value_formatted = format_value(node['value1'], depth + 1)
                new_value_formatted = format_value(node['value2'], depth + 1)
                
                result_lines.append(
                    f"{current_indent}  - {node_key}: {old_value_formatted}"
                    )
                result_lines.append(
                    f"{current_indent}  + {node_key}: {new_value_formatted}"
                    )

    result = "{\n" + "\n".join(result_lines) + "\n" + current_indent + "}"
    return result'''