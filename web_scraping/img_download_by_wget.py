import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os
import re
import wget


url="https://books.toscrape.com/"

def fetch(url):
    try:
        response= requests.get(url,headers={"User-Agent": "Mozilla/5.0"},timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"failed to fetch data\n{e}")
        return []

    soup= BeautifulSoup(response.text,"html.parser")
    images= soup.find_all("div",class_="image_container")

    if not os.path.exists("images"):
        os.makedirs("images",exist_ok=True)

    for image in images[:10]:
        image_name= image.find("a").find("img").get("alt").strip()
        img_name= re.sub(r"[^\w\-_.]","_",image_name).replace(" ","_")
        img_url= urljoin(url , image.find("a").find("img")["src"])
         
        filename= f"{img_name}.jpg"
        filepath= os.path.join("images",filename)

        wget.download(img_url,filepath)

    print("Downloaded images succesfully")

fetch(url)