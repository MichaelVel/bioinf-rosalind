from os import remove, path
from shutil import copy
import pickle

from options import Template
from web.uniprot import download_from_uniprot

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
def copy_template(template: Template, location: str):
    input_file = f"{Template.folder()}/{template.template_file()}"
    copy(input_file, location)

# -- From source utilities
def get_from_uniprot(filename: str) -> str:
    """Get data from the uniprot datasource, the function tries to 
    cache the results of the querys, but if one of the writes failed 
    then at a new run the data will be downloaded again.
    """

    file_cached = filename.replace(".txt", "_CACHE.fasta")

    if path.isfile(file_cached):
        return parseInput(file_cached)
    
    input = parseInput(filename)
    data = download_from_uniprot(input)

    writeCache(file_cached, '\n'.join(data))

    return ''.join(data)

# -- Dump utilities
def dump_cookies(filename, data: dict[str,str]):
    with open(filename, 'wb') as f: pickle.dump(data,f)

def load_cookies(filename) -> dict[str,str]:
    with open(filename, 'rb') as f: return  pickle.load(f)

def update_cookies(filename, data: dict[str,str]):
    with open(filename, 'w+b') as f:
        data_loaded =pickle.load(f)
        pickle.dump({**data_loaded,**data},f)

