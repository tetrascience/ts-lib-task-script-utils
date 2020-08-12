import typing as t

def file_type_check(filename: str, expected_type: t.Union[str, list]):
  """
   filename also support S3 object key because you will capture the file extension
   e.g. /tetrasicence/123456/example-file1.txt
        example-file1.txt
   these two should be both supported
   expected_type can be a string or array 
  """
  # get the extension from filename
  extension = filename[::-1].strip().split('.')[0].lower()
  try:
    if type(expected_type) == str:
      # lower case both the extension and expected_type, do a string match
      assert extension == expected_type.lower()
    elif type(expected_type) == list:
      assert extension in [file_type.lower() for file_type in expected_type]
  except AssertionError:
    print(f"The pipeline is expecting the file type to be {expected_type}, but the provided file has a file type of {extension}")

if __name__ == "__main__":
  file_type_check('/tetrasicence/123456/example-file1.txt', 'txt')
  file_type_check('example-file1.txt', 'txt')
  file_type_check('/tetrasicence/123456/example-file1.txt', ['txt', 'xlsx', 'csv'])
  file_type_check('/tetrasicence/123456/example-file1.txt', ['xlsx', 'csv'])
