import shelve

with shelve.open("shelve_test") as fruit:
    fruit["orange"] = "orange is a citrus fruit"
    fruit["apple"] = "apple a day keeps the doctor away"
    fruit["lemon"] = "lemon is a citrus fruit"
    fruit["jackfruit"] = "i love jackfruit"

    print(fruit["lemon"])
    print(fruit["apple"])
    fruit["lime"] = "Great with tequila"

    for snack in fruit:
        print(snack + ": " + fruit[snack])
    while True:
        dict_key = input("Please enter your fruit ")
        if dict_key == "quit":
            break
        if dict_key in fruit:
            description = fruit[dict_key]
            print(description)
        else:
            print("We don't have a "+dict_key)
print(fruit)
