# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:33
# @Author  : ChowRunFa
# @File    : csv2json.py
# @Software: PyCharm

import csv
import json
with open('info.csv', newline='', encoding='gbk') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [dict(row) for row in reader]
with open('info.json', 'w', encoding='UTF-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)
