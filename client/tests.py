from pathlib import Path
from string import Template
import pytest
import sys

from utilities import Location
from web.exercises import Exercise
from input_output import writeCache

class Test():
    def __init__(self, id: str, loc: Location) -> None:
        self.id = id
        self.test_path = f"solution_tests/{id}.py"
        self.challenge_path = f"{loc.package()}/{loc.module()}/{id}.py"
        self.module = f"{loc.package()}.{loc.module()}" 
        self.d = {
            "module": self.module,
            "file": id,
            "test_data": "",
            "expected": "", 
        }

    def test_exist(self) -> bool:
        return Path(self.test_path).exists()

    def test_remove(self) -> None:
        if self.test_exist():
            Path(self.test_path).unlink()

    def create_test(self):
        result = ""
        exercise = Exercise(self.id)
        exercise.get()
        self.d["test_data"] = exercise.sample_dataset()
        self.d["expected"] = exercise.sample_output()

        with open("templates/test_template.py", "r") as f:
            src = Template(f.read())
            result = src.substitute(self.d)

        writeCache(self.test_path, result) 
        if self.test_exist():
            print(f"Created test at {self.test_path}")
        else:
            print("Failed to create test")

    def run_test(self):
        if not self.test_exist():
            raise Exception(f"The test in {self.test_path} doesn't exists")

        sys.exit(pytest.main(["-x", self.test_path]))

        

