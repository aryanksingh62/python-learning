import requests
import argparse

def fetch_profile(username):
    url=f"https://api.github.com/users/{username}"
    url2= f"https://api.github.com/users/{username}/repos"
    try:
        response= requests.get(url,timeout=10)
        response.raise_for_status()
        data= response.json()

        response2= requests.get(url2,timeout=10)
        response2.raise_for_status()
        data2= response2.json()

        if not data:
            print(f"there is no data in profile of {username}")
            return
        
        total_repos= data["public_repos"]
        followers= data["followers"]
        following= data["following"]
        
        languages={}
        if not data2:
            print(f"this {username} has no repos")
        else:
            for i in data2:
                if i["language"]!= None:
                    languages.setdefault(i["language"],0)
                    languages[i["language"]] +=1
        
        
        print(f"username: {username}")
        print(f"repos count:{total_repos}\nfollowers: {followers}\nfollowing: {following}")
        
        if languages:
            print(f"top language: {max(languages, key=languages.get)}")
        else:
            print(f"repos has no languages")

    except requests.RequestException as e:
        print(f"User not found\n{e}")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    args= parser.parse_args()
    username= args.username
    fetch_profile(username)
