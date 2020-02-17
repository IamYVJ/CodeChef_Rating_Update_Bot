from Rating_Scraper_Selenium import get_source_selenium
from Rating_Scraper_Requests import get_source_requests
from Extract_Data import getData
from Check_Data import check_Data
from Write_Data import write_Data
from Send_Email import sendEmail

def driver():
    username = "yvj1809"
    data_new = get_source_selenium(username)
    data_new = getData(data_new)
    data_old = check_Data(username)
    if data_old==False:
        write_Data(username, data_new)
        print(data_new)
        print( data_new.extend(['NA', 'NA']))
        sendEmail(username,data_new)
    else:
        print("SAME2")
        if data_old==data_new:
            print("SAME")
driver()