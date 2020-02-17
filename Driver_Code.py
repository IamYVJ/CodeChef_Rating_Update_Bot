from Rating_Scraper_Selenium import get_source_selenium
from Rating_Scraper_Requests import get_source_requests
from Extract_Data import getData
from Check_Data import check_Data
from Write_Data import write_Data
from Send_Email import sendEmail
from Credentials import return_credentials
from time import sleep

def check(username, extraction_method, email_ID, sender_email_ID, sender_email_ID_password):
    data_new = ""
    if extraction_method==0:
        data_new = get_source_selenium(username)
    elif extraction_method==1:
        data_new = get_source_requests(username)
    data_new = getData(data_new)
    data_old = check_Data(username)
    if data_old==False:
        write_Data(username, data_new)
        data = data_new.extend(['NA', 'NA'])
        sendEmail(username, data, email_ID, sender_email_ID, sender_email_ID_password)
        return False
    else:
        if data_old==data_new:
            return False
        else:
            write_Data(username, data_new)
            data = data_new.extend(data_old)
            sendEmail(username, data, email_ID, sender_email_ID, sender_email_ID_password)
            return True

def driver():
    credentials = return_credentials()

    username = credentials[0]
    email_ID = credentials[1]
    sender_email_ID = credentials[2]
    sender_email_ID_password = credentials[3]
    extraction_method = credentials[4]
    flag = credentials[5]

    while True:
        update = check(username, extraction_method, email_ID, sender_email_ID, sender_email_ID_password)
        if update and flag==False:
            break
        sleep(600)
    
driver()