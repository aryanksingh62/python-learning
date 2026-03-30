import os
import json

FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME,"r",encoding="utf-8") as f:
        return json.load(f)
    
def save_movies(movies):
    with open(FILENAME,"w",encoding="utf-8") as f:
        return json.dump(movies,f,indent=2)

def add_movies():
    title=input("Enter movie name:").strip().lower()
    genre=input("Enter movie type:").strip().lower()
    rating=float(input("Enter the rating bwteen(1-10):").strip())
    movies = load_movies()
    n_movie={}
    for i in movies:
        if i["title"]==title:
            return print("movie name already exist")
                
    n_movie["title"]=title
    n_movie["genre"]=genre
    n_movie["rating"]=rating 
    movies.append(n_movie)
    save_movies(movies)
    print("Movie added Sucessfully")

def view_movies():
    movies=load_movies()
    if not movies:
        print("file is empty")
        return
    
    print(f"Title | Genre | Rating")
    print("-"*30)
    for i in movies:
        print(F"{i["title"]} | {i["genre"]} | {i["rating"]}")

def search_movies():
    movies=load_movies()
    term=input("enter the movie term(title or genre):").lower()
    results=[i for i in movies if term in i["title"].lower() or term in i["genre"].lower()]
    if not results:
        print("No matching results")
        return
    for movie in results:
        print(f"{movie["title"]} | {movie["genre"]} | {movie["rating"]}")

def run_movies():

    while True:
        print("My_Movies")
        print("1. Add Movies")
        print("2. View All Movies")
        print("3. Search Movies")
        print("4. Exit")
        choice=input("enter choice from(1-4):")
        match choice:
            case "1":add_movies()
            case "2":view_movies()
            case "3":search_movies()
            case "4":break
            case _: print("enter valid choice")
if __name__=="__main__":
    run_movies()