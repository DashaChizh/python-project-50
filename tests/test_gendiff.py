from pathlib import Path
from gendiff.scripts.core import generate_diff


def get_test_data_path(filename1, filename2):
    filepath1 = Path(__file__).parent / "test_data" / filename1
    filepath2 = Path(__file__).parent / "test_data" / filename2
    return str(filepath1), str(filepath2)


def test_generate_diff_json():
    filepath1, filepath2 = get_test_data_path("file1.json", "file2.json")
    actual = generate_diff(filepath1, filepath2)
    
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert actual == expected


def test_generate_diff_yaml():
    filepath1, filepath2 = get_test_data_path("file1.yaml", "file2.yaml")
    actual = generate_diff(filepath1, filepath2)
    
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert actual == expected


def test_with_json_and_yaml():
    filepath1, filepath2 = get_test_data_path("file1.json", "file2.yaml")
    actual = generate_diff(filepath1, filepath2)
    
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert actual == expected
    
    filepath1, filepath2 = get_test_data_path("file1.yaml", "file2.json")
    actual = generate_diff(filepath1, filepath2)
    assert actual == expected

