import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os
import re

os.makedirs("images",exist_ok=True)
url="https://books.toscrape.com/"

total_book_count=10
try:
    response= requests.get(url,headers={"User-Agent": "Mozilla/5.0"},timeout=10)
    response.raise_for_status()

    soup= BeautifulSoup(response.text,"html.parser")
    images= soup.find_all("div",class_="image_container")

    for image in images[:10]:
        image_name= image.find("a").find("img").get("alt").strip()
        img_name= re.sub(r"[^\w\-_.]","_",image_name).replace(" ","_")
        img_url= urljoin(url , image.find("a").find("img")["src"])
        img_data= requests.get(img_url).content
        
        filename= f"images/{img_name}.jpg"
        with open(filename,"wb") as file:
            file.write(img_data)
        
    print("Downloaded images succesfully")

except requests.RequestException as e:
    print(f"failed to fetch data\n{e}")