import json
from evaluation import to_official, official_evaluate

path="D:/chromedownload/ATLOP/dataset/docred"
f=open("D:/southeast/course/web/result.json","r")
tmp=json.load(f)

for i in tmp:
    i["h_idx"]=int(i["h_idx"])
    i["t_idx"]=int(i["t_idx"])

print(official_evaluate(tmp,path))