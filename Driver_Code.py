from Rating_Scraper_Selenium import get_source_selenium
from Rating_Scraper_Requests import get_source_requests
from Extract_Data import getData
from Check_Data import check_Data
from Write_Data import write_Data
from Send_Email import sendEmail
from Credentials import return_credentials, make_credentials
from time import sleep
import time
from Clear_Screen import clear_Screen

def check(username, extraction_method, email_ID, sender_email_ID, sender_email_ID_password):
    i = 0
    while True:
        if extraction_method==0:
            data_new = get_source_selenium(username)
        elif extraction_method==1:
            data_new = get_source_requests(username)
        data_new = getData(data_new)[0]
        if len(data_new)<1:
            if i>5:
                print("Failed to get Data for {}".format(username))
                return False
            else:
                i+=1
                continue
        else:
            break
    data_old = check_Data(username)
    if data_old==False:
        write_Data(username, data_new)
        data = [data_new] + ['NA']
        sendEmail(username, data, email_ID, sender_email_ID, sender_email_ID_password)
        print("Initial Data Updated for {} with Rating {}".format(username, data_new))
        return False
    else:
        if data_old==data_new:
            print("No Change In Data for {} with Rating {}".format(username, data_new))
            return False
        else:
            write_Data(username, data_new)
            data = [data_new] + [data_old]
            sendEmail(username, data, email_ID, sender_email_ID, sender_email_ID_password)
            print("Data Updated for {}".format(username))
            print("Old Rating: {}".format(data_old))
            print("New Rating: {}".format(data_new))
            return True

def print_time():
    localtime = time.asctime( time.localtime(time.time()) )
    print(localtime)

def print_dash():
    print("------------------------------------------------------------------------------------")

def start_print(username):

    print()
    print()
    print_dash()
    print()
    print("                      CodeChef Ratings Update Bot")
    print("                              YVJ Systems")
    print()
    if username!="":
        for i in range(0, 31-len(username)):
            print(" ", end = "")
        print("CodeChef User: {}".format(username))
        print()

def driver():
    credentials = return_credentials()

    if credentials[0]=="":
        start_print("")
        print_dash()
        print()
        credentials = make_credentials()
        sleep(2)
        clear_Screen()

    username = credentials[0]
    email_ID = credentials[1]
    sender_email_ID = credentials[2]
    sender_email_ID_password = credentials[3]
    extraction_method = credentials[4]
    flag = credentials[5]
    
    start_print(username)

    while True:
        print_dash()
        print_time()
        update = check(username, extraction_method, email_ID, sender_email_ID, sender_email_ID_password)
        if update and flag==False:
            break
        sleep(600)
    
driver()