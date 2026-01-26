from pathlib import Path
from gendiff import generate_diff


def get_test_data_path(filename1, filename2):
    filepath1 = Path(__file__).parent / "test_data" / filename1
    filepath2 = Path(__file__).parent / "test_data" / filename2
    return str(filepath1), str(filepath2)


def test_nested_json():
    filepath1, filepath2 = get_test_data_path(
        "file1_nested.json", 
        "file2_nested.json"
    )
    
    actual = generate_diff(filepath1, filepath2)
    
    expected_start = "{\n    common: {\n      + follow: false"
    
    assert actual.startswith(expected_start)
    assert "  - setting2: 200" in actual
    assert "  - setting3: true" in actual
    assert "  + setting3: null" in actual
    assert "  + setting5:" in actual
    assert "      key5: value5" in actual


def test_nested_yaml():
    filepath1, filepath2 = get_test_data_path(
        "file1_nested.yaml", 
        "file2_nested.yaml"
    )
    
    actual = generate_diff(filepath1, filepath2)
    
    assert "  - setting2: 200" in actual
    assert "  - setting3: true" in actual
    assert "  + setting3: null" in actual
