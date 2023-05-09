import pathlib
import sys
from types import ModuleType

from importlib import import_module

# Set the directory name
default_name = "rosalind_workspace"
subdirs = [".session", "data", "tests", "solutions", "output", "templates"]

test_template = '''\
from $module import $file

class TestClass:
    def test_answer(self):
        """ For some kind of problems the template has some problems, in 
        particular when testing results given in floating point, the test 
        will fail and is necessary to modify the test in the testing 
        directory"""
  
        data: str = "$test_data"
        expected: str = "$expected"

        result: str = ${file}.main(data)
        assert expected == result
'''

config_template = '''\
DATA_FOLDER = "data"
TEMPLATE_FOLDER = "templates"
SOLUTION_FOLDER = "solutions"
TEST_FOLDER = "tests"
OUTPUT_FOLDER = "output"
'''

def is_valid_workspace() -> bool:
    cwd_name = pathlib.Path.cwd()

    config_file_path = pathlib.Path(cwd_name) / "config.py"
    if not config_file_path.exists(): return False

    for subdir in subdirs:
        subdir_path = pathlib.Path(cwd_name) / subdir
        if not subdir_path.exists(): return False

    return True

def create_file(path: pathlib.Path, contents: str):
    with open(path, "w") as file: file.write(contents)
    
def create_workspace(dir_name: str | None = None):
    if not dir_name: dir_name = default_name

    pathlib.Path(dir_name).mkdir()
    for subdir in subdirs:
        subdir_path = pathlib.Path(dir_name) / subdir
        subdir_path.mkdir()
        print(f"Subdirectory {subdir_path} created.")

    config_path = pathlib.Path(dir_name) / "config.py"
    test_template_path = pathlib.Path(dir_name) / "templates" / "test_template.py"

    create_file(test_template_path, test_template)
    create_file(config_path, config_template)


def load_config() -> ModuleType:
    if not is_valid_workspace():
        raise Exception("The current folder is not a valid rosalind-cli workspace")

    cwd_name = pathlib.Path.cwd()
    sys.path.append(str(cwd_name))
    config = import_module("config")
    return config


def load_solution_module(id: str) -> ModuleType:
    config = load_config()
    
    solution_module = import_module(f"{config.SOLUTION_FOLDER}.{id}")

    if "main" not in dir(solution_module):
        raise Exception("Solution file doesnt contains main function")

    return solution_module

