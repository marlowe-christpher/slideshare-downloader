#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import urllib
import urllib.request
from bs4 import BeautifulSoup

num = 0
url = input()
save_dir = os.getcwd()#現在のディレクトリを取得
req = urllib.request.Request(url) #requestを使って、webから取得
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml") #要素を抽出

for a in soup.find_all(class_= "slide_image"):
    print(a.get('data-full'))
    num += 1
    str_num = str(num)#str型に変換
    str_num_fill = str_num.zfill(4)#番号を4桁にして、空いている桁は0埋め
    urllib.request.urlretrieve(a.get('data-full'), save_dir+"/slide-"+str_num_fill+".jpg")
    print("done")