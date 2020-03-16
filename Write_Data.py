from OSDetect import osDetect

def file_path(username):
    syst = osDetect()

    if syst=='W':
        return 'Data\\' + str(username) + ".txt"

    elif syst=='L':
        return 'Data/'+ str(username) + ".txt"

    elif syst=='M':
        return 'Data/'+ str(username) + ".txt"


def write_Data(username, data):
    path = file_path(username)
    try:
        file = open(path, "w")
    except:
        return False
    finally:
        file.write(data)
        file.close()
        return True