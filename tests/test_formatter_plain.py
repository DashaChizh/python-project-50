import json
import yaml
from gendiff import generate_diff
from gendiff.formatter.plain import format_plain, format_value
from gendiff.diff_builder import build_diff
from pathlib import Path


def test_format_value():
    assert format_value("text") == "'text'"
    assert format_value(123) == "123"
    assert format_value(-7) == "-7"
    assert format_value(True) == "true"
    assert format_value(False) == "false"
    assert format_value(None) == "null"
    
    assert format_value({"a": 1}) == "[complex value]"
    assert format_value([1, 2, 3]) == "[complex value]"
    assert format_value({"a": {"b": [1, 2]}}) == "[complex value]"


def test_format_plain_simple():
    diff = [
        {'key': 'a', 'type': 'unchanged', 'value': 1},
        {'key': 'b', 'type': 'removed', 'value': 2},
        {'key': 'c', 'type': 'added', 'value': 3},
        {'key': 'd', 'type': 'changed', 'value1': 4, 'value2': 5},
    ]
    
    result = format_plain(diff)
    actual = result.split('\n')
    
    expected = [
        "Property 'b' was removed",
        "Property 'c' was added with value: 3",
        "Property 'd' was updated. From 4 to 5",
    ]
    
    assert actual == expected


def test_format_plain_nested():
    diff = [
        {
            'key': 'common',
            'type': 'nested',
            'children': [
                {'key': 'follow', 'type': 'added', 'value': False},
                {'key': 'setting2', 'type': 'removed', 'value': 200},
                {
                    'key': 'setting6',
                    'type': 'nested',
                    'children': [
                        {
                            'key': 'doge',
                            'type': 'nested',
                            'children': [
                                {'key': 'wow', 'type': 'changed', 'value1': '', 'value2': 'so much'}
                            ]
                        }
                    ]
                }
            ]
        }
    ]
    
    result = format_plain(diff)
    
    assert "Property 'common.follow' was added with value: false" in result
    assert "Property 'common.setting2' was removed" in result
    assert "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'" in result


def test_format_plain_complex_value():
    diff = [
        {'key': 'setting5', 'type': 'added', 'value': {'key5': 'value5'}},
        {'key': 'group3', 'type': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}},
    ]
    
    result = format_plain(diff)
    
    assert "Property 'setting5' was added with value: [complex value]" in result
    assert "Property 'group3' was added with value: [complex value]" in result


def test_generate_diff_plain_full_example():  
    file1_path = Path(__file__).parent / "test_data" / "file1_nested.json"
    file2_path = Path(__file__).parent / "test_data" / "file2_nested.json"
    
    result = generate_diff(str(file1_path), str(file2_path), 'plain')
    
    expected = [
        "Property 'common.follow' was added with value: false",
        "Property 'common.setting2' was removed",
        "Property 'common.setting3' was updated. From true to null",
        "Property 'common.setting4' was added with value: 'blah blah'",
        "Property 'common.setting5' was added with value: [complex value]",
        "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'",
        "Property 'common.setting6.ops' was added with value: 'vops'",
        "Property 'group1.baz' was updated. From 'bas' to 'bars'",
        "Property 'group1.nest' was updated. From [complex value] to 'str'",
        "Property 'group2' was removed",
        "Property 'group3' was added with value: [complex value]",
    ]
    
    actual = result.split('\n')

    assert actual == expected
