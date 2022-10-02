from importlib.resources import path
from xml.etree.ElementPath import xpath_tokenizer
import requests
import bs4
import shutil
import urllib.request as req
import os

def crawler(url):
    request=req.Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    })
    with req.urlopen(request) as response:
        origin_data=response.read().decode("utf-8")

    bs4_data=bs4.BeautifulSoup(origin_data, "html.parser")
    print(bs4_data)

internet=input()
crawler(internet)