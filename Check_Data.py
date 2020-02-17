from OSDetect import osDetect

def file_path(username):
    syst = osDetect()

    if syst=='W':
        return 'Data\\' + str(username) + ".txt"

    elif syst=='L':
        return 'Data/'+ str(username) + ".txt"

    elif syst=='M':
        return 'Data/'+ str(username) + ".txt"


def check_Data(username):
    path = file_path(username)
    try:
        file = open(path, "r")
    except:
        return False
    else:
        data = []
        data.append(file.readline()[:-1])
        data.append(file.readline())
        file.close()
        return data