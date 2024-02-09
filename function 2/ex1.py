from data import data

movies = data()

def score(movie_name):
    has = False
    for movie in movies:
        if movie_name == movie["name"]:
            has = True
            if movie["imdb"] > 5.5:
                print("True")
    if not has:
        print("we don't have movie in our data")
movie = input("which movie do you wanna see?\n")
score(movie)