import os
import requests
from bs4 import BeautifulSoup as bs


def GetAllLinksImages(url):
    html = requests.get(url).text
    soup = bs(html, "html.parser")
    soup = soup.find("div", {"class": "reading-content"})
    images = soup.find("p", {"id": "arraydata"})
    links = images.text.split(",")

    return links


def Downloader(urls, name, cap=1):
    for i in range(1, len(urls)):
        print(f"downloading: {name}/{cap:03d}/{i:03d}")

        os.makedirs(f"{name}/{cap:03d}", exist_ok=True)
        img = requests.get(urls[i]).content

        with open(f"{name}/{cap:03d}/{i:03d}.jpg", "wb") as f:
            f.write(img)
