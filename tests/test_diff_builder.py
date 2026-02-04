from gendiff.scripts.diff_builder import build_diff


def test_build_diff_simple():
    data1 = {"a": 1, "b": 2}
    data2 = {"a": 1, "c": 3}
    
    diff = build_diff(data1, data2)
    
    assert len(diff) == 3
    assert diff[0]['key'] == 'a'
    assert diff[0]['type'] == 'unchanged'
    assert diff[1]['key'] == 'b'
    assert diff[1]['type'] == 'removed'
    assert diff[2]['key'] == 'c'
    assert diff[2]['type'] == 'added'