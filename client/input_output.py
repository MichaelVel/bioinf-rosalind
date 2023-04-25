from os import remove
from shutil import copy
from enum import Enum

# ---- Input / Output utilities 
def parseInput(filename: str) -> str:
    with open(filename, 'r') as f: return f.read()

def writeCache(filename: str, data: str) -> None:
    try:
        with open(filename, 'a') as f: 
            f.write(data)
    except Exception:
        remove(filename)

# --- Template utilities
class Template(str,Enum):
    list = "list"
    map = "map"
    simple = "simple"

    def template_file(self) -> str:
        match self.value:
            case "list": return "starter_list.py"
            case "map": return "starter_map.py"

        return "starter.py"

    @staticmethod
    def folder() -> str:
        return "templates"

def copy_template(template: Template, location: str):
    input_file = f"{Template.folder()}/{template.template_file()}"
    copy(input_file, location)

