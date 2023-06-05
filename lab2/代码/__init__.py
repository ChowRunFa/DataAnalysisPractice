# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 10:00
# @Author  : ChowRunFa
# @File    : __init__.py.py
# @Software: PyCharm
import difflib

import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    head = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
    }
    try:
        resp = requests.get(url, timeout=30,headers= head)
        # resp.raise_for_status()
        resp.encoding = 'utf-8'
        return resp.text
    except:
        return ""


def fillUnivList(soup):
    file = open('links.csv', mode='w')
    file.write('link\n')
    Alist  = soup.findAll('div',class_='section hero-result-box mod-bg clearfix')
    linkre = re.compile('<a href="(.*?)">')
    for line in Alist:
        lst = str(line).replace('\xa0', '').split('\n')
        # print(lst)
        for href in lst:
            link = linkre.findall(href)
            if  len(link) > 0:
                print(link)
                file.write(str(link[0]))
                file.write('\n')
def main(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)

url = 'https://db.18183.com/wzry/'
main(url)