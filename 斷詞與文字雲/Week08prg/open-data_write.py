# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") #取得台灣大學網站的原始碼(HTML,CSS,JS)
# print(data)
import urllib.request as request
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src) as response:
    data=json.load(response) # 利用 json 模組處理 json 資料格式
#print(data)
# 公司名稱列表出來
clist=data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")