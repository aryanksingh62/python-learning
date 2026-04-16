import requests
from pathlib import Path
from bs4 import BeautifulSoup

def title_extracter(url):
    try:
        response= requests.get(url,headers={"User-Agent": "Mozilla/5.0"},timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text,"html.parser")

        if soup.find("title"):
            title= soup.find("title").text.strip()
            print(f"{url} ➡️ {title}")
        else:
            print(f"{url} ➡️ No title found")

    except requests.RequestException as e:
        print(e)

def input_list(input_file):
    if not Path(input_file).exists():
        print("Invalid file")
        return
    
    with open(input_file,"r",encoding="utf-8") as file:
        for row in file:
            link = row.strip()
            if not link:
                continue
            if not link.startswith(("http://","https://")):
                link= "https://" + link
            title_extracter(link)


if __name__=="__main__":
    input_list("list_url.txt")