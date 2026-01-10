from gendiff import generate_diff


def test_generate_diff():
    filepath1 = 'tests/test_data/file1.json'
    filepath2 = 'tests/test_data/file2.json'

    result = generate_diff(filepath1, filepath2)

    expected = '''{
    - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
    }'''

    assert result == expected