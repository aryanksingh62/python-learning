import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

url="https://quotes.toscrape.com/"

def fetch_data(url):
    response= requests.get(url,headers={"User-Agent": "Mozilla/5.0"},timeout=10)
    response.raise_for_status()

    soup= BeautifulSoup(response.text,"html.parser")
    quotes= soup.select("div.quote")

    quotes_data=[]
    for q in quotes[:5]:
        text= q.find("span",class_="text").text.strip('"\u201c\u201d')
        author= q.find("small",class_="author").text
        quotes_data.append((text,author))

    return quotes_data

def create_image(text,author,index):
        if not os.path.exists("quotes"):
            os.makedirs("quotes")

        img= Image.new("RGB",(800,400),color="white")
        draw= ImageDraw.Draw(img)

        font_quote= ImageFont.load_default()
        font_author= ImageFont.load_default()

        wrapped= textwrap.fill(text,width=60)
        
        draw.text((50,150),wrapped,fill="black",font=font_quote)
        y_author = 150 + wrapped.count('\n') * 15 + 40
        draw.text((50,y_author), f"- {author}", fill="gray", font=font_author)
        
        filename= f"quotes/quote_{index+1}.png"
        img.save(filename)
        print(f"{filename} saved succesfullly")


def main():
    quote_data= fetch_data(url)
    for i, (text,author) in enumerate(quote_data):
            create_image(text,author,i)

if __name__== "__main__":
    main()