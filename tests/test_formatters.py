from gendiff.formatter.stylish import format_stylish


def test_format_stylish():
    diff = [
        {'key': 'a', 'type': 'unchanged', 'value': 1},
        {'key': 'b', 'type': 'removed', 'value': 2},
        {'key': 'c', 'type': 'added', 'value': 3}
    ]
    
    result = format_stylish(diff)
    assert "    a: 1" in result
    assert "  - b: 2" in result
    assert "  + c: 3" in result