from collections.abc import Callable
from enum import Enum
from types import ModuleType
from importlib import import_module

from uniprot import get_from_uniprot
from input_output import parseInput, writeCache
# ----- Source utilities
SOURCE_CALLBACKS: dict[str, Callable[[str], str]]= {
        "uniprot": get_from_uniprot,
}

def get_data_from_source(source: str) -> Callable[[str], str]:
    if source not in SOURCE_CALLBACKS:
        raise Exception("Unimplemented data source stream")
    return SOURCE_CALLBACKS[source]

# ------ Location utilities
class Location(Enum):
    STRONGHOLD = "lib.stronghold"
    ARMORY = "lib.armory"
    TEXTBOOK = "lib.textbook_track"

def load_solution_module(
        id: str,
        location: Location = Location.STRONGHOLD
) -> ModuleType:
    name = f"{location.value}.{id}"
    return import_module(name)
