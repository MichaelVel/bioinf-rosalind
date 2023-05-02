from bs4 import BeautifulSoup, Tag, NavigableString
from requests_toolbelt import MultipartEncoder
import requests

from web.exceptions import (
        UnauthorizedAccessException,
        ExerciseNotFoundException,
        WrongAnswerException,
)

class Exercise:
    def __init__(self, id: str, cookies: None | dict[str,str] = None) -> None:
        self.url = f"https://rosalind.info/problems/{id}/"
        self.id = id
        self.session = requests.session()
        self.get_request = None
        self.post_request = None
        self.soup = None

        if cookies: 
            self.session.cookies.update(cookies)


    def get(self) -> dict[str,str]:
        self.get_request = self.session.get(self.url)

        if self.get_request.status_code == 404:
            raise ExerciseNotFoundException(
                    f"The problem with id {id} doesn't exist")

        self.soup = BeautifulSoup(self.get_request.text, 'html.parser')

        return self.session.cookies.get_dict()
    

    def submit(self, output_filename: str) -> dict[str,str]:
        cookie = self.session.cookies.get("csrftoken")
        m = MultipartEncoder( fields = {
            'output_file': 
                ('solution.txt',open(output_filename, 'rb'), 'text/plain'),
            #'code': ('solution.txt',open(code_filename, 'rb'), 'text/plain'),
            'csrfmiddlewaretoken': (None, cookie)})

        header = {'Content-Type': m.content_type, 'referer': self.url}

        self.post_request = self.session.post(
                self.url,
                headers = header,
                data = m)

        if self.post_request.status_code == 403:
            raise UnauthorizedAccessException(
                    "Please login to publish your results")

        self.soup = BeautifulSoup(self.post_request.text, 'html.parser')

        if not self.soup.find_all('div', class_="alert-success"):
            raise WrongAnswerException()

        return self.session.cookies.get_dict()


    def problem_dataset(self) -> str:
        # This particular request doesn't set cookies, so it's not necessary 
        # return the session cookies.
        dataset_url = f"{self.url}dataset/"
        self.get_request = self.session.get(dataset_url)

        if self.get_request.url != dataset_url:
            raise UnauthorizedAccessException(
                    "Please login to publish your results")
        
        return self.get_request.text

    def sample_dataset(self) -> str:
        if not self.soup:
            raise Exception("called method before a request have been made")

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
        if not self.soup:
            raise Exception("called method before a request have been made")

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




