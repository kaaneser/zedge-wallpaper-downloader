from bs4 import BeautifulSoup
import requests, os, json

def downloadImage(image, count, search):
    image_url = requests.get(f"https://www.zedge.net/api-zedge-web/browse/download/{image}")
    content = image_url.content
    str_content_url = content.decode("utf-8").replace('"', "")
    
    with open(f"Download/{search}/resim{count}.jpg", "wb") as img:
        image_binary = requests.get(str_content_url).content
        img.write(image_binary)

    

arama = input("İndirmek istediğiniz fotoğraf adı girin: ")
if (os.path.exists("Download\\{}".format(arama)) == False):
    os.mkdir("Download\\{}".format(arama))
offset = 48
url_forjson = requests.get(f"https://www.zedge.net/api-zedge-web/browse/search?query={arama}&contentType=wallpapers")

json_info = json.loads(url_forjson.content)

cursorList = json_info["navigation"]
count = 0

for cursor in range(len(cursorList['all_cursors'])):
    offset = cursorList['all_cursors'][cursor]
    url = requests.get(f"https://www.zedge.net/api-zedge-web/browse/search?query={arama}&cursor={offset}&section=search-wallpapers-{arama}&contentType=wallpapers")

    items_json = json.loads(url.content)

    for image in items_json["items"]:
        downloadImage(image["downloadReference"], count, arama)
        count += 1
