# ts-lib-task-script-utils <!-- omit in toc -->

[![Build Status](https://travis-ci.com/tetrascience/ts-lib-task-script-utils.svg?token=7onD2L3nEXMByQUNdxv1&branch=master)](https://travis-ci.com/tetrascience/ts-lib-task-script-utils)

Utility functions for task scripts

- [Installation](#installation)
- [Troubleshooting installation](#troubleshooting-installation)
- [Adding a Function to the Repo](#adding-a-function-to-the-repo)
- [Example](#example)

## Installation

1. Set up your [ssh key](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).
2. Do `pipenv install -e 'git+ssh://git@github.com/tetrascience/ts-lib-task-script-utils.git#egg=ts-ts-util'`
3. In the file you want to use the function, do `from module_name import function_name` (for example: `from common import check_file_type`)
4. Use function: `function_name()` if imported as in step 5
5. Alternatively, you can also import the function by using `import module_name` (for example: `import common`)
6. Use function: `module_name.function_name()` if imported as in step 7

## Troubleshooting installation
We have found that some users run into the following error upon installing with pipenv:
```
ERROR: Requested ts-lib-task-script-utils from git+ssh://****@github.com/tetrascience/ts-lib-task-script-utils.git#egg=ts-ts-util (from -r /var/folders/4p/9yhw2cfx23n39w_9dhhy1yl00000gn/T/pipenv-46s_v3k4-requirements/pipenv-f4o6ngps-requirement.txt (line 1)) has different name in metadata: 'ts-lib-task-script-utils
```
This is often caused by incorrect initial installation of the package.
If you encounter this error, please take the following steps to resolve it:
1. Clear pipenv environment: `pipenv --rm`
2. Delete `pipfile.lock`
3. Delete the `ts-ts-util` or `ts-lib-task-script-utils` line from `pipfile` and save
4. Re-run `pipenv install -e 'git+ssh://git@github.com/tetrascience/ts-lib-task-script-utils.git#egg=ts-ts-util'`

## Adding a Function to the Repo

1. For the function you want to add, make sure you have `__init__.py` in every folder through its path. 
2. In `__init__.py`, add `from .file_path import function_name`. This allows others to use `common` to import your function (see step 5 above)
3. Add the function's dependencies to `setup.py` under `REQUIRES` (versions can be set [like so](https://stackoverflow.com/questions/8161617/how-can-i-specify-library-versions-in-setup-py)). Combined with including the `-e` flag in pipenv install, package dependencies are installed. For more information, see [this](https://pipenv-fork.readthedocs.io/en/latest/advanced.html#pipfile-vs-setup-py).
4. Please follow an active verb form for function names (i.e. `check_file_type` vs `file_type_check`)

## Example

See [task-scripts/common/tecan-sunrise-raw-to-ids/v1.0.0](https://github.com/tetrascience/ts-lib-protocol-script/tree/development/task-scripts/common/tecan-sunrise-raw-to-ids/v1.0.0). 

You can find `ts-ts-util` package in `Pipfile` and `Pipfile.lock`

In `main.py`, the function `check_file_type` is imported from `common`. 
