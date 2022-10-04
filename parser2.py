from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import os
from os.path  import basename
import requests

directory = os.path.join(os.path.expanduser('~'), 'parser', 'images')

var = "horror"
url = "https://in.pinterest.com/search/pins/?q=" + var 
ScrollNumber = 3 
sleepTimer = 1    

options = webdriver.ChromeOptions() 
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(url)
images = []
count = 0
for _ in range(10):
    for _ in range(1,ScrollNumber):
        driver.execute_script("window.scrollTo(1,100000)")
        print("scrolling")
        time.sleep(sleepTimer)

    soup = BeautifulSoup(driver.page_source,'html.parser')

    for link in soup.find_all('img'):
        if link.get('src') not in images:
            images.append(link.get('src'))
            print(link.get('src'))
            with open(basename(link.get('src')), "wb") as f:
            	f.write(requests.get(link.get('src')).content)
            count += 1
print(count)