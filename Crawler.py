from importlib.resources import path
from xml.etree.ElementPath import xpath_tokenizer
import requests
import bs4
import shutil
import urllib.request as req
import os

def crawler(url):
    request=req.Request(url, headers={

        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "cookie": "cf_clearance=GCD4ZbLm95BUgRp7ij_JXkC86hzEa4ulcjL.Svv1nD0-1664602975-0-150; __cf_bm=S7mer56OBOfGlsen_fWiM2OOW3jLwCNdhPMlvbADa0k-1664678978-0-AUrbkmp3sRFeIt4CxkS3++qcEzF6a1SqrQ4Okl2LNbqf1XiMzAvsIXGwrx+Aeyv0PY/7b0sHDx9RAGiQcqwIjrD+rdG9D7dWIFTi+AA3XhGY/MfEVVLxEzgL8ZyNWnTt4w==",
        "pragma": "no-cache",
        "referer": "https://steamdb.info/sales/",
        "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    })
        

    with req.urlopen(request) as response:
        origin_data=response.read().decode("utf-8")

    bs4_data=bs4.BeautifulSoup(origin_data, "html.parser")
    print(bs4_data)

internet=input()
crawler(internet)