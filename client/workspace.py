import pathlib
from types import ModuleType

from importlib import import_module

# Set the directory name
default_name = "rosalind_workspace"
subdirs = [".session", "data", "tests", "solutions", "output", "templates"]

def is_valid_workspace() -> bool:
    cwd_name = pathlib.Path.cwd()

    config_file_path = pathlib.Path(cwd_name) / "config.py"
    if not config_file_path.exists(): return False

    for subdir in subdirs:
        subdir_path = pathlib.Path(cwd_name) / subdir
        if not subdir_path.exists(): return False

    return True

def create_workspace(dir_name: str | None = None):
    if not dir_name: dir_name = default_name

    pathlib.Path(dir_name).mkdir()
    for subdir in subdirs:
        subdir_path = pathlib.Path(dir_name) / subdir
        subdir_path.mkdir()
        print(f"Subdirectory {subdir_path} created.")

    file_path = pathlib.Path(dir_name) / "config.py"
    with open(file_path, "w") as file:
        file.write("print('Hello, World!')\n")
        print(f"File {file_path} created.")

def load_config() -> ModuleType:
    if not is_valid_workspace():
        raise Exception("The current folder is not a valid rosalind-cli workspace")

    config = import_module("config")
    return config


def load_solution_module(id: str) -> ModuleType:
    config = load_config()

    solution_module = import_module(f"{config.SOLUTION_FOLDER}.{id}")

    if "main" not in dir(solution_module):
        raise Exception("Solution file doesnt contains main function")

    return solution_module

