import requests

def get_source_requests(username):
    url = 'https://www.codechef.com/users/' + str(username)
    source_code = requests.get(url)
    return source_code.text