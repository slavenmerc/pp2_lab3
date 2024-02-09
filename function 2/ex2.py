from data import data

movies = data()

def goodmovie():
    for movie in movies:
        if(movie["imdb"] > 5.5):
            print(movie)

goodmovie()