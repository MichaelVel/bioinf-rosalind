from requests_toolbelt import MultipartEncoder
import requests

from exceptions import UnauthorizedAccessException

def login(username: str, password: str) -> dict[str,str]:
    referer = "https://rosalind.info/problems/locations/"
    session = requests.session()

    # This get is necessary because Rosalind requires a csrftoken that 
    # you only get after visits the link.
    session.get("https://rosalind.info/accounts/login/")

    m = MultipartEncoder( fields = {
        'username': (None,username),
        'password': (None,password),
        'csrfmiddlewaretoken': (None, session.cookies.get('csrftoken')),})
    header = {'referer': referer, 'Content-Type': m.content_type }

    response = session.post(
            "https://rosalind.info/accounts/login/", 
            headers = header,
            data = m)

    if response.url != 'https://rosalind.info/problems/list-view/':
        # There are multiple ways to check if the login was succesful, 
        # but i choose the fact that rosalind redirects you to this 
        # particular link.
        raise UnauthorizedAccessException(
                "Failed to login. Wrong username and/or password")
    
    return session.cookies.get_dict()

