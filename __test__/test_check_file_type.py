import pytest
from common.check_file_type import check_file_type

def test_check_file_type():
    check_file_type('/tetrascience/123456/example-file1.txt', 'txt')
    check_file_type('example-file1.txt', 'txt')
    check_file_type('/tetrascience/123456/example-file1.xlsx', ['txt', 'xlsx', 'csv'])
    with pytest.raises(SystemExit):
        check_file_type('/tetrascience/123456/example-file1.txt', ['xlsx', 'csv'])
