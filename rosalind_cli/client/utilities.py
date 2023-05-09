from collections.abc import Callable

from .input_output import get_from_uniprot

# ----- Source utilities
SOURCE_CALLBACKS: dict[str, Callable[[str], str]]= {
        "uniprot": get_from_uniprot,
}

def get_data_from_source(source: str) -> Callable[[str], str]:
    if source not in SOURCE_CALLBACKS:
        raise Exception("Unimplemented data source stream")
    return SOURCE_CALLBACKS[source]



