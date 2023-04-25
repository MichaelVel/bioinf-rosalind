from os import path
import re

from requests import get
import input_output as io

UNIPROT_URL = "http://www.uniprot.org/uniprot/"
UNIPROT_NOT_FOUND = "The id {id} of file {file} not found in Uniprot"

# rgx taken from https://www.uniprot.org/help/accession_numbers
UNIPROT_ID_RGX = re.compile(
    "[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}")

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
        return io.parseInput(file_cached)
    
    input = io.parseInput(filename)
    input_from_uniprot: list[str] = []

    for id in input.split():
        valid_id = validate_id(id)
        url = f"{UNIPROT_URL}{valid_id}.fasta"  
        print(f"Downloading from {url}")
        id_data = get(url)
        if id_data.status_code in (404, 400):
            raise Exception(UNIPROT_NOT_FOUND.format(id,filename))
        input_from_uniprot.append(id_data.text)

    io.writeCache(file_cached, '\n'.join(input_from_uniprot))

    return ''.join(input_from_uniprot)
