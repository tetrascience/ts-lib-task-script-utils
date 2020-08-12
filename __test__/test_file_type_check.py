import pytest
from common.file_type_check import file_type_check

def test_file_type_check():
  file_type_check('/tetrasicence/123456/example-file1.txt', 'txt')
  file_type_check('example-file1.txt', 'txt')
  file_type_check('/tetrasicence/123456/example-file1.xlsx', ['txt', 'xlsx', 'csv'])
  file_type_check('/tetrasicence/123456/example-file1.txt', ['xlsx', 'csv'])
