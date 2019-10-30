# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:50:44 2019

@author: kfc399
"""

import urllib.request as request
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src) as response:
    data=json.load(response) # 利用 json 模組處理 json 資料格式
#print(data)
# 公司名稱列表出來
clist=data["result"]["results"]
for company in clist:
        print(company["公司名稱"])