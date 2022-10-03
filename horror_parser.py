from urllib.request import Request, urlopen
import os
import time
from bs4 import BeautifulSoup
import requests
from PIL import Image
from os.path  import basename

dir = os.path.dirname(os.path.abspath(__file__))

url = 'https://www.freepik.com/free-photos-vectors/horror'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url,headers=hdr)
page = urlopen(req)

soup = BeautifulSoup(page, 'html.parser')

images = soup.find_all("img", class_="lzy")
for i in range(100):
       images_url = images[i]['data-src'] 
       with open(basename(images_url), "wb") as f:
            f.write(requests.get(images_url).content)
