#structue/getAllLink.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def getAllLink (link):
    driver = webdriver.Chrome()
    driver.get(link)
    continue_link = driver.find_elements(By.TAG_NAME,"a")
    print(len(continue_link))
    print("Following are the link present in the webpage")
    for totals in continue_link:
        print(totals.get_attribute('href'))