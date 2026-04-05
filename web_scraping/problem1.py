from bs4 import BeautifulSoup
import requests

url="https://en.wikipedia.org/wiki/Python_(programming_language)"

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    soup= BeautifulSoup(response.text,"html.parser")
    h2=[]
    headers= soup.find_all("h2")
    for header in headers:
        clean= header.get_text(strip=True).replace("[edit]","").strip()
        if clean:
            h2.append(clean)
                
    print("total header in this page:",len(h2))
    print("first 10 section title:")
    for h in h2[:10]:
        print(h)

except requests.RequestException as e:
    print(f"Failed to fetch data:\n {e}")