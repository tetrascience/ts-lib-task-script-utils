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
5. In the file you want to use the function, do `import module_name` (for example: `import common`)
6. Use function: `module_name.function_name`
   
## Adding Function to Repo
1. For the function you want to add, make sure you have `__init__.py` in every folder through its path. 
2. In `__init__.py`, add `from .file_path import function_name`

## Example
See [task-scripts/common/unchained-labs-lunatic-util/v1.0.0](https://github.com/tetrascience/ts-lib-protocol-script/tree/DE-1213-packaging-ts-lib-task-script-utils-repo/task-scripts/common/unchained-labs-lunatic-util/v1.0.0). 

You can find `task-util` package in `Pipfile` and `Pipfile.lock`

In `src/` folder, `lunatic_util`.py uses the function `convert_to_float` in `common` module. 