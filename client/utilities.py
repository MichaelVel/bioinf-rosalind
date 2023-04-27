from collections.abc import Callable
from enum import Enum
from types import ModuleType
from importlib import import_module

from uniprot import get_from_uniprot
from input_output import (
    parseInput, 
    writeCache, 
    Template,
    copy_template,
)

# ----- Source utilities

SOURCE_CALLBACKS: dict[str, Callable[[str], str]]= {
        "uniprot": get_from_uniprot,
}

def get_data_from_source(source: str) -> Callable[[str], str]:
    if source not in SOURCE_CALLBACKS:
        raise Exception("Unimplemented data source stream")
    return SOURCE_CALLBACKS[source]


# ------ Location utilities

class Location(str,Enum):
    STRONGHOLD = "sth"
    ARMORY = "arm"
    TEXTBOOK = "txt"

    def module(self) -> str:
        match self.value:
            case "sth": return "stronghold"
            case "arm": return "armory"
            case "txt": return "textbook_track"
        
        # Unreachable
        return ""

    @staticmethod
    def package() -> str:
        return "lib"


def load_solution_module(
        id: str,
        location: Location = Location.STRONGHOLD
) -> ModuleType:
    return import_module(f"{location.module()}.{id}", package=Location.package())

