#存活探测
import requests
for i in range(1,255):
    url = f"http://192-168-1-{i}.awd.bugku.cn/"
    try:
        html = requests.get(url,timeout=2)
        print(url)
    except:
        pass