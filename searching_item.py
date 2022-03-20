shopping_list = ["Milk","chocolate","pasta","spam","eggs"]
item_to_find = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print("Item found at index {}".format(index))
