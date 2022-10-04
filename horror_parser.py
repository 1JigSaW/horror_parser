from urllib.request import Request, urlopen
import os
import time
from bs4 import BeautifulSoup
import requests
from PIL import Image
from os.path  import basename
import requests

path = '/home/jigsaw/parser/images'
url = 'https://www.freepik.com/free-photos-vectors/horror'
hdr = {'User-Agent': 'Mozilla/5.0'}
count = 0
for i in range(1, 10):
    if i > 1:
        url += '/' + str(i)
    print(url)
    req = Request(url,headers=hdr)
    page = urlopen(req)

    soup = BeautifulSoup(page, 'html.parser')

    images = soup.find_all("img", class_="lzy")
    for i in range(50):
        images_url = images[i]['data-src']
        print(images_url[:images_url.find("?")])
        count += 1
        with open(basename(images_url[:images_url.find("?")]), "wb") as f:
            f.write(requests.get(images_url).content)


