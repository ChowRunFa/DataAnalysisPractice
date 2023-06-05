# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 10:46
# @Author  : ChowRunFa
# @File    : Info.py
# @Software: PyCharm
import time
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


Name =''
Str = ''
def fillUnivList(soup):
    global Name,Str
    divs  = soup.find('div',class_='otherinfo-datapanel')
    attrs = soup.find('div',class_='attr-list')
    names = soup.find('div',class_='name-box')
    name = names.find('h1')
    Name = name.text
    Str += Name
    ddre =  re.compile('<dd><span class="star star-(.*?)"></span></dd>')
    dds = attrs.findAll('dd')
    for dd in dds:
        Str += ','+ddre.findall(str(dd))[0]
    lis = divs.findAll('li')
    for li in lis:
        Str += ',' +li.text.split("：")[1].strip()

def main(url):
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        fillUnivList(soup)

def getInfo():
    file = open('info.csv', mode='w')
    file.write(
        '序号,英雄名字,生存能力,攻击伤害,技能效果,上手难度,最大生命,最大法力,物理攻击,法术攻击,物理防御,物理减伤率,法术防御,法术减伤率,移速,物理护甲穿透,法术护甲穿透,攻速加成,暴击几率,暴击效果,物理吸血,法术吸血,冷却缩减,攻击范围,韧性,生命回复,法力回复\n')

    linkSuffix = []
    for line in open('links.csv', 'r', encoding='utf-8'):
        linkSuffix.append(line.strip())  # 一次读一行，并且内存不会溢出，去除空行或者空格
    linkSuffix.remove(linkSuffix[0])
    # print(linkSuffix)
    global target, Str
    for index,suffix in enumerate(linkSuffix):
        # suffix = '/wzry/hero/16364.html'
        Str = ''
        target = 'https://db.18183.com/' + suffix
        time.sleep(1)
        main(target)
        file.write(str(index)+','+Str)
        file.write('\n')
        print(str(index)+','+Str)

getInfo()