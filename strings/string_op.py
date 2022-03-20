magicians = ['tharika','Tanusri','Sumathy']
for magic in magicians:
    print(f"{magic.title()} , is awesome !")
    print(f"I can't wait to see your next trick,{magic.title()}\n")

squares = []
for i in range(1,11):
    square = i ** 2
    squares.append(square)
print(squares)

names = ['Tony','Hul','Benedict','Harry','Hermoine','Ron']
#for name in names:
print(names[2:])
print(names[2:4])

num = [1,2,3,4,5,6,7,8,9,10]
print(num[1: :2])

fav_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print(f"first threitems in the list : \n{fav_foods[:3]}.")
print(f"Three items from middle of list:\n{fav_foods[1:4]}")
print(f"Laste three items :\n{fav_foods[-3:]}")
