from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def collect_text():
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.wikipedia.org/")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchInput"))
        )

        search_box= driver.find_element(By.ID,"searchInput")
        search_box.send_keys("Hindi cinema")
        search_box.send_keys(Keys.RETURN)

        WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,"firstHeading")))

        soup= BeautifulSoup(driver.page_source,"html.parser")
        list_of_para=[]
        paragraphs= soup.select("div.mw-content-ltr.mw-parser-output p")

        count=0
        for p in paragraphs:
            text= p.get_text()
            if text.strip():
                list_of_para.append(text.strip())
                count+=1
            if count==3:
                break
        print(f"✅All paragraphs colected succesfully")
        print()

        list_of_headings=[]
        headings= soup.select("div.mw-content-ltr.mw-parser-output h2,h3,h4")
        for heading in headings:
            list_of_headings.append(heading.get_text().strip())
        print(f"✅All heading collected succesfully")
        print()

    except Exception as e:
        print(f"failed to scrape the data\n{e}")

    finally:
        driver.quit()

    return list_of_para , list_of_headings

def save_to_txt(paragraphs,headings,output_file):
    try:
        with open(output_file,"w") as f:
            f.write("First 3 Paragraphs:\n\n")
            for row in paragraphs:
                f.write(f"{row}\n\n")
            f.write("\n\n")
            f.write("Headings:\n\n")

            for i in headings:
                f.write(f"{i}\n")
        print(f"✅succesfully saved data into {output_file}")
    
    except Exception as e:
        print(f"failed to save data into .txt file{e}\n")

if __name__=="__main__":
    file= "scrap.txt"
    print("Scraping and Collecting data starting...\n")
    paragraphs,headings= collect_text()
    save_to_txt(paragraphs,headings,file)