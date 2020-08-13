# ts-lib-task-script-utils

Utility functions for task scripts

- [ts-lib-task-script-utils](#ts-lib-task-script-utils)
  - [Installation](#installation)
  - [Adding Function to Repo](#adding-function-to-repo)
  - [Example](#example)

## Installation
1. Make sure you have private access to this repo. 
2. Set up your [ssh key](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh). 
3. Do `pipenv install git+ssh://git@github.com/tetrascience/ts-lib-task-script-utils.git#egg=ts-ts-util` (If clone error occurs, try `pipenv install -e git+git@github.com:tetrascience/ts-lib-task-script-utils.git#egg=ts-ts-util`)
4. Do `pipenv lock -r > requirements.txt`
5. In the file you want to use the function, do `from module_name import function_name` (for example: `from common import file_type_check`)
6. Use function: `function_name()` if imported as in step 5
7. Alternatively, you can also import the function by using `import module_name` (for example: `import common`)
8. Use function: `module_name.function_name()` if imported as in step 7
   
## Adding Function to Repo
1. For the function you want to add, make sure you have `__init__.py` in every folder through its path. 
2. In `__init__.py`, add `from .file_path import function_name`. This allows others to use `common` to import your function (see step 5 above)
3. Add the function's dependencies to `setup.py` under `REQUIRES` (versions can be set [like so](https://stackoverflow.com/questions/8161617/how-can-i-specify-library-versions-in-setup-py)). Combined with including `"-e ." = "*"` in the Pipfile, package dependencies are installed. For more information, see [this](https://github.com/pypa/pipenv/issues/209#issuecomment-337409290) response.

## Example
See [task-scripts/common/tecan-sunrise-raw-to-ids/v1.0.0](https://github.com/tetrascience/ts-lib-protocol-script/tree/development/task-scripts/common/tecan-sunrise-raw-to-ids/v1.0.0). 

You can find `ts-ts-util` package in `Pipfile` and `Pipfile.lock`

In `main.py`, the function `file_type_check` is imported from `common`.