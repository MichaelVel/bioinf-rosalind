from bs4 import BeautifulSoup, Tag, NavigableString
import requests

class ProblemParser:
    def __init__(self, id: str) -> None:
        url = f"https://rosalind.info/problems/{id}/"
        self.r = requests.get(url)
        if self.r.status_code == 404:
            raise Exception(f"The problem with id {id} doesn't exist")
        
        self.soup = BeautifulSoup(self.r.text, 'html.parser')

    def sample_dataset(self) -> str:
        dataset = self.soup.find(id="sample-dataset")
        if not isinstance(dataset, Tag):
            return ""
        dataset = dataset.find_next()
        text = ""
        if isinstance(dataset, NavigableString):
            text = dataset.text 
        elif isinstance(dataset, Tag):
            text = dataset.string

        return text.strip() if text else ""

    def sample_output(self) -> str:
        dataset = self.soup.find(id="sample-output")
        if not isinstance(dataset, Tag):
            return ""
        dataset = dataset.find_next()
        text = ""
        if isinstance(dataset, NavigableString):
            text = dataset.text 
        elif isinstance(dataset, Tag):
            text = dataset.string

        return text.strip() if text else ""



