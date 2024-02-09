from data import data

movies = data()

def avarage(category):
    sum = 0
    devide = 0
    for movie in movies:
        if category == movie["category"]:
            sum += movie["imdb"]
            devide += 1
    try:
        return "average in this category is " + str(sum / devide)
    except:
        return "we don't have this category"
    
name = input("choose a category\n")
print(avarage(name))