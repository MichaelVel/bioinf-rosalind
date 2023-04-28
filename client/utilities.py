from collections.abc import Callable
from types import ModuleType
from importlib import import_module

from input_output import get_from_uniprot
from options import Location

# ----- Source utilities
SOURCE_CALLBACKS: dict[str, Callable[[str], str]]= {
        "uniprot": get_from_uniprot,
}

def get_data_from_source(source: str) -> Callable[[str], str]:
    if source not in SOURCE_CALLBACKS:
        raise Exception("Unimplemented data source stream")
    return SOURCE_CALLBACKS[source]


# ------ Location utilities
def load_solution_module(
        id: str,
        location: Location = Location.STRONGHOLD
) -> ModuleType:
    return import_module(f"{location.module()}.{id}", package=Location.package())

