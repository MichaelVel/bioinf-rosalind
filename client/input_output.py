from os import remove
from typing import Iterable

# ---- Input / Output utilities 
def parseInput(filename: str) -> str:
    with open(filename, 'r') as f: return f.read()

def writeCache(filename: str, data: Iterable[str]) -> None:
    try:
        with open(filename, 'a') as f: 
            for entry in data: f.write(entry)
    except Exception:
        remove(filename)
