available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"
                   ]
current_choice = "-"
computer_parts = [] # create an empty list
valid_choice = []
for i in range(1, len(available_parts)+1):
    valid_choice.append(str(i))
print(valid_choice)
while current_choice != '0':
    if current_choice in "123456":
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print(f"Revoving {current_choice.title()}")
            computer_parts.remove(chosen_part)
        else:
            print(f"adding {current_choice}")
            computer_parts.append(chosen_part)
        print("Your list now ontains {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)
