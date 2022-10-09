from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import os
from os.path  import basename
import requests
import re

def pin_find(href):
    return href and re.compile("/pin/").search(href)

directory = os.path.join(os.path.expanduser('~'), 'parser', 'images')

var = "scary"
old_url = "https://in.pinterest.com/search/pins/?q=" + var 
ScrollNumber = 3 
sleepTimer = 1    

options = webdriver.ChromeOptions() 
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(old_url)

soup = BeautifulSoup(driver.page_source,'html.parser')
# soup = BeautifulSoup(driver.page_source,'html.parser')
# for link in soup.find_all(href=pin_find):
#     print(link.get('href'))
images = []
link_name = ''
count = 0
n = 1
pins = soup.find_all(href=pin_find)
names = soup.find_all('img')
folder_images = [x for x in os.listdir() if os.path.isfile(x)]
while True:
    soup = BeautifulSoup(driver.page_source,'html.parser')
    for link, im in zip(pins, names):
        link_name = re.findall('/([A-z0-9]+.jpg$)', im['src'])
        if len(link_name) != 0:
            link_name = link_name[0]

        if link.get('href') not in images and link_name not in folder_images:
            print(link.get('href'))
            if link.get('href')[0] == 'h':
                url = link.get('href')
            else:
                url = 'https://in.pinterest.com' + link.get('href')
            driver.get(url)
            time.sleep(sleepTimer)
            soup = BeautifulSoup(driver.page_source,'html.parser')
            try:
                print(soup.find_all('img')[0].get('src')) 
            except IndexError:
                driver.execute_script("window.history.go(-1)")
                continue
            print(soup.find_all('img')[0].get('src'))  
            picture = soup.find_all('img')[0].get('src')
            with open(basename(picture), "wb") as f:
                f.write(requests.get(picture).content)      
            driver.execute_script("window.history.go(-1)")
            time.sleep(sleepTimer)
            soup = BeautifulSoup(driver.page_source,'html.parser')
            images.append(link.get('href'))
            count += 1
            print(f'-----Stats: {count}, {images}')
            print(n)
            

    for _ in range(1, 20):
        driver.execute_script("window.scrollTo(1,100000)")
        print('scroll')
        time.sleep(sleepTimer)

    pins = soup.find_all(href=pin_find)
    names = soup.find_all('img')
