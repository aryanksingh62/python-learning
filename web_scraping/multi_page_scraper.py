import requests
from urllib.parse import urljoin
import json
from bs4 import BeautifulSoup

url="https://books.toscrape.com"
BOOK_FILE= "book.json"

def fetch_books(url):
    total_count=70
    data= []
    while url:
        try:
            response= requests.get(url,headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            response.raise_for_status()

            soup= BeautifulSoup(response.text,"html.parser")
            books= soup.find_all("article",class_="product_pod")

            for book in books:
                name= book.find("h3").find("a").get("title")
                price= book.find("p",class_="price_color").get_text().encode("latin-1").decode("utf-8")
                data.append({"title":name,"price":price})

                if len(data)==total_count:
                    return data
                

            next= soup.find("li",class_="next")
            next_button= next.find("a") if next else None

            url = urljoin(url, next_button.get("href")) if next_button else None
    
        except requests.RequestException as e:
            print(f"Failed to fetch data\n{e}")
            return []
        
    return data

def save_to_json(data):
    if not data:
        print("ther is no data to save")
        return
    with open(BOOK_FILE,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
        print("books data stored succcesfully")
        return
    
def  main():
    data= fetch_books(url)
    save_to_json(data)
    print("total no. of book stored:",len(data))

if __name__=="__main__":
    main()
