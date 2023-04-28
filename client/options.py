from enum import Enum

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
