import requests

def get_source_requests(username):
    url = 'https://www.codechef.com/users/' + str(username)
    source_code = requests.get(url)
    rawSource = ""
    try:
        for i in source_code:
            try:
                rawSource = rawSource + i
            except:
                pass
    except:
        pass
    return rawSource