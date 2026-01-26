import json


def format_json(diff):
    result = build_json_structure(diff)
    return json.dumps(result, indent=2)


def build_json_structure(diff):
    result = []
    
    for node in diff:
        node_type = node['type']
        key = node['key']
        
        if node_type == 'nested':
            children = build_json_structure(node['children'])
            result.append({
                'key': key,
                'type': 'nested',
                'children': children
            })
        
        elif node_type in ('unchanged', 'added', 'removed'):
            result.append({
                'key': key,
                'type': node_type,
                'value': node['value']
            })
        
        elif node_type == 'changed':
            result.append({
                'key': key,
                'type': 'changed',
                'old_value': node['value1'],
                'new_value': node['value2']
            })
    
    return result