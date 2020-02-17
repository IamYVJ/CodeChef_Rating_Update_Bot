from getpass import getpass

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

def make_credentials():
    username_CodeChef = input("Enter CodeChef Username: ")
    email_ID = input("Enter Receiver's Email-ID: ")
    sender_email_ID = input("Enter Sender's Email-ID: ")
    sender_email_ID_password = getpass("Enter Sender's Email-ID Password: ")
    extraction_method = int(input("Enter Extraction Method (0/1): "))
    no_stop = input("Enter Run Time (Once/Infy): ")
    if no_stop=="Once":
        no_stop = False
    else: 
        no_stop = True
    credentials = [
                username_CodeChef,
                email_ID,
                sender_email_ID,
                sender_email_ID_password,
                extraction_method,
                no_stop
                ]
    return credentials
