import requests
import json
from pathlib import Path

def collect_pokemon(url):
    result=[]
    count=1
    while url:
        try:
            response= requests.get(url,timeout=10)
            response.raise_for_status()
            data= response.json()

            if not data:
                print(f"there is no data in {url}")
                return []
            
            for names in data["results"]:
                poke_name= names["name"]
                url2= names["url"]

                try:
                    response2= requests.get(url2,timeout=10)
                    response2.raise_for_status()
                    data2= response2.json()
                    if not data2:
                        print(f"No data found of {poke_name}")
                        continue

                    poke_weight= data2["weight"]
                    poke_height= data2["height"]
                    poke_type= [i["type"]["name"] for i in data2["types"]]
                    result.append({"name":poke_name,"type":poke_type,"weight":poke_weight,"height":poke_height})
            
                except requests.RequestException as e:
                    print(f"Failed to access the data of {poke_name}\n{e}")

            print(f"pokemon deatils on page {count} collected succesfully✅")
            count+=1
            if count==9:
                break

            next_url= data["next"] if data["next"] else None
            url = next_url if next_url else None
        
        except requests.RequestException as e:
            print(f"failed to access the pokeapi.co\n{e}")
            return []
    return result

def save_to_json(data,output_file):

    if not data:
        print("there is no data to store")
        return
    with open(output_file,"w",encoding="utf-8") as file:
        json.dump(data,file,indent=2)
        print(f"✅✅succesfully saved all pokemon details to {output_file}")

def main():
    URL=f"https://pokeapi.co/api/v2/pokemon"
    OUTPUTFILE="poke_details.json"
    print("started collecting pokemon details from pokeapi.co....")
    data= collect_pokemon(URL)
    save_to_json(data,OUTPUTFILE)

if __name__=="__main__":
    main()