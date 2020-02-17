
username_CodeChef = ""
email_ID = ""

sender_email_ID = ""
sender_email_ID_password = ""

extraction_method = 1 # 0 - Selenium, 1 - Requests

no_stop = True #False to stop at one change, True to keep running

def return_credentials():
    credentials = [
                username_CodeChef,
                email_ID,
                sender_email_ID,
                sender_email_ID_password,
                extraction_method,
                no_stop
                ]
    return credentials
