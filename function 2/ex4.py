from data import data

movies = data()

def avarage(takes):
    sum = 0
    devide = 0
    for take in takes:
        has = False
        for movie in movies:
            if take == movie["name"]:
                has = True
                sum += movie["imdb"]
                devide += 1
    if not has:
        print("Sorry we don't have movie " + take)
    if devide == 0:
        devide = 1
    return sum / devide

takes = input()
takes = takes.split(", ")
print(avarage(takes))