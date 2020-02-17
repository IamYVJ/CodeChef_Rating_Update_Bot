from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as OptionsCr
from OSDetect import osDetect

global driver
driver = ""


def get_source_selenium(username):

    syst = osDetect()

    if syst=='W':
        options = Options()
        options.headless = True
        driver = wd.Firefox(executable_path = r'drivers\Windows\geckodriver.exe', options=options)

    elif syst=='M':
        driver = wd.Chrome()

    elif syst=='L':
        options = Options()
        options.headless = True
        driver = wd.Firefox(executable_path = r'drivers/Linux/geckodriver', options=options)

    url = 'https://www.codechef.com/users/' + str(username)
    driver.get(url)
    source_code = driver.page_source
    driver.close()
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


