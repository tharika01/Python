import shelve
"""blt = ["bacon","lettue","tomato","bread"]
beans_on_toast = ["beans","toast"]
scrambled_eggs = ["eggs","butter","milk"]"""
soup = ["tin of soup"]
#pasta = ["pasta","cheese"]

with shelve.open('recipes') as recipes:
    """recipes["blt"] = blt
    recipes["beans_on_toast"] = beans_on_toast
    recipes["scrambled_eggs"] = scrambled_eggs
    recipes["pasta"] = pasta
    recipes["soup"] = soup"""

    recipes["soup"] = soup
    recipes.sync()
    soup.append("cream")

    temp_list = recipes["pasta"]
    temp_list.append("tomato")
    recipes['pasta'] = temp_list
    for snack in recipes:
        print(snack, recipes[snack])

