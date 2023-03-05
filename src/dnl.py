from bs4 import BeautifulSoup as bs
import requests


def GetAllLinksImages(url):
    html = requests.get(url).text
    soup = bs(html, "html.parser")
    soup = soup.find("div", {"class": "reading-content"})
    images = soup.find("p", {"id": "arraydata"})
    links = images.text.split(",")

    return links
