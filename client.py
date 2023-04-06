from sys import argv
from importlib import import_module
from types import ModuleType

def parseInput(filename: str) -> str:
    with open(filename, 'r') as f: return f.read()

HOW_TO = """\
Usage: python client.py <datafile> <modulename>
    <datafile>   : a file in format txt: <data>.txt
    <modulename> : the name of a file in `lib/`. 
                   for lib/example.py -> example
"""

def run():
    filename = ""
    modulename = ""
    
    try:
        filename = argv[1]
        modulename = f"lib.{argv[2]}"
    except: 
        print(HOW_TO)
        return 

    try:
        solution = import_module(modulename)
    except Exception as e:
        print(f"Failed import of lib/{argv[2]} file.")
    else:
        input = parseInput(filename)
        solution = solution.main(input)
        print(solution)


if __name__ == "__main__":
    run()


