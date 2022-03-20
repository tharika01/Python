cities = []
with open("cities.txt","r") as city_file:
    for city in city_file:
        cities.append(city)
print(cities)
for city in cities:
    print(city,end = " ")

imelda = "More Mayhem", "Imelda May", "2011",(
    (1,"Pulling with the rug"),(2,"Psycho"),(3,"Mayhem"))
with open("imelda.txt","w") as imelda_file:
    print(imelda, file = imelda_file)

with open("imelda.txt","r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)

