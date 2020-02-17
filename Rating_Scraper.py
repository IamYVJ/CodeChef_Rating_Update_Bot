from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as OptionsCr
import json
from OSDetect import osDetect

global driver
driver = ""


def get_source(username):

    syst = osDetect()

    if syst=='W':
        options = Options()
        # options.headless = True
        driver = wd.Firefox(executable_path = r'drivers\Windows\geckodriver.exe', options=options)

    elif syst=='M':
        driver = wd.Chrome()

    elif syst=='L':
        options = Options()
        options.headless = True
        driver = wd.Firefox(executable_path = r'drivers/Linux/geckodriver', options=options)

    url = 'https://www.codechef.com/users/' + str(username)
    # url = "https://www.google.co.in"
    driver.get(url)
    source_code = driver.page_source
    time.sleep(0.5)
    driver.close()
    # print(source_code)
    rawSource = ""
    try:
        for i in source_code:
            try:
                rawSource = rawSource + i
            except:
                print("ERROR")
                pass
    except:
        pass
    # print(rawSource)
    return(rawSource)


def getData(rawSource):
    soup = BeautifulSoup(rawSource, 'html5lib')
    ratings = []
    for row in soup.findAll('div', attrs = {'class':'rating-number'}):
        # print(str(row.text))
        ratings.append(str(row.text))

    return ratings



import requests

def get_html(url): #to store html
    f=open('htmlcode.txt','w')
    r = requests.get(url)
    f.write(r.text)
    f.close()

# print(get_source("yvj1809"))
r = get_source("yvj1809")
jsonData(r)
# get_html()


