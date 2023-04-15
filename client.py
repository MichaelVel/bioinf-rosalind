import re
from sys import argv
from os import path, remove
from importlib import import_module
from typing import Iterable
from requests import get

HOW_TO = """\
Usage: python client.py <flags> <datafile> <modulename>
    --FLAGS 
    -u --uniprot : when set, will get data from uniprot.org using the
                   the ids from <datafile>
    --ARGS
    <datafile>   : a file in format txt: <data>.txt
    <modulename> : the name of a file in `lib/`. 
                   for lib/example.py -> example
"""

UNIPROT_FLAGS = {"-u", "--uniprot"}
UNIPROT_URL = "http://www.uniprot.org/uniprot/"
UNIPROT_NOT_FOUND = "The id {id} of file {file} not found in Uniprot"

# rgx taken from https://www.uniprot.org/help/accession_numbers
UNIPROT_ID_RGX = re.compile(
    "[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}")

def parseInput(filename: str) -> str:
    with open(filename, 'r') as f: return f.read()

def writeCache(filename: str, data: Iterable[str]) -> None:
    try:
        with open(filename, 'a') as f: 
            for entry in data: f.write(entry)
    except Exception:
        remove(filename)

def validate_id(id: str) -> str:
    id_validated = re.match(UNIPROT_ID_RGX,id)
    if not id_validated:
        raise Exception(f"id {id} not contains a valid UniProtKB id")

    return id_validated[0]
    

def get_from_uniprot(filename: str) -> str:
    """Get data from the uniprot datasource, the function tries to 
    cache the results of the querys, but if one of the writes failed 
    then at a new run the data will be downloaded again.
    """

    file_cached = filename.replace(".txt", "_CACHE.fasta")

    if path.isfile(file_cached):
        return parseInput(file_cached)
    
    input = parseInput(filename)
    input_from_uniprot: list[str] = []

    for id in input.split():
        valid_id = validate_id(id)
        url = f"{UNIPROT_URL}{valid_id}.fasta"  
        print(f"Downloading from {url}")
        id_data = get(url)
        if id_data.status_code in (404, 400):
            raise Exception(UNIPROT_NOT_FOUND.format(id,filename))
        input_from_uniprot.append(id_data.text)

    writeCache(file_cached, input_from_uniprot)

    return ''.join(input_from_uniprot)

def run():
    filename = ""
    modulename = ""
    u_flag = any(f in argv for f in UNIPROT_FLAGS)

    try:
        # This could be generalized to remove all flags.
        argv_copy = [x for x in argv if x not in UNIPROT_FLAGS]
        filename = argv_copy[1]
        modulename = f"lib.{argv_copy[2]}"
    except: 
        print(HOW_TO) 
        return 

    try:
        solution = import_module(modulename)
    except Exception as e:
        print(e)
        print(f"Failed import of lib/{argv[2]} file.")
    else:
        input = get_from_uniprot(filename) if u_flag else parseInput(filename)
        
        solution = solution.main(input)
        print(solution)


if __name__ == "__main__":
    run()


