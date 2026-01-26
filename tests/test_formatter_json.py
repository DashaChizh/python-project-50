import json
from gendiff.formatter.json import format_json


def test_format_json_simple_unchanged():
    diff = [
        {
            'key': 'name',
            'type': 'unchanged',
            'value': 'John'
        }
    ]
    
    result = format_json(diff)
    parsed_result = json.loads(result)
    
    expected = [
        {
            'key': 'name',
            'type': 'unchanged',
            'value': 'John'
        }
    ]
    
    assert parsed_result == expected


def test_format_json_simple_added():
    diff = [
        {
            'key': 'age',
            'type': 'added',
            'value': 30
        }
    ]
    
    result = format_json(diff)
    parsed_result = json.loads(result)
    
    expected = [
        {
            'key': 'age',
            'type': 'added',
            'value': 30
        }
    ]
    
    assert parsed_result == expected


def test_format_json_simple_removed():
    diff = [
        {
            'key': 'city',
            'type': 'removed',
            'value': 'Moscow'
        }
    ]
    
    result = format_json(diff)
    parsed_result = json.loads(result)
    
    expected = [
        {
            'key': 'city',
            'type': 'removed',
            'value': 'Moscow'
        }
    ]
    
    assert parsed_result == expected
    

def test_format_json_changed_value():

    diff = [
        {
            'key': 'price',
            'type': 'changed',
            'value1': 100,
            'value2': 150
        }
    ]
    
    result = format_json(diff)
    parsed_result = json.loads(result)
    
    expected = [
        {
            'key': 'price',
            'type': 'changed',
            'old_value': 100,
            'new_value': 150
        }
    ]
    
    assert parsed_result == expected


def test_format_json_nested_structure():
    diff = [
        {
            'key': 'user',
            'type': 'nested',
            'children': [
                {
                    'key': 'name',
                    'type': 'unchanged',
                    'value': 'Alice'
                },
                {
                    'key': 'active',
                    'type': 'changed',
                    'value1': False,
                    'value2': True
                }
            ]
        }
    ]
    
    result = format_json(diff)
    parsed_result = json.loads(result)
    
    expected = [
        {
            'key': 'user',
            'type': 'nested',
            'children': [
                {
                    'key': 'name',
                    'type': 'unchanged',
                    'value': 'Alice'
                },
                {
                    'key': 'active',
                    'type': 'changed',
                    'old_value': False,
                    'new_value': True
                }
            ]
        }
    ]
    
    assert parsed_result == expected