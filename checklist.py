import os
checklist = list()

# colors
Blue = '\033[94m'
Cyan = '\033[96m'
Green = '\033[92m'
Yellow = '\033[93m'
reset = '\033[0m'

# welcone message
print(f"{Cyan}Welcome to Captain Rainbow's Color Checklist{reset}")

# define functions
# lists all items
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# creates item in list
def create(item):
    checklist.append(item)

# reads item in list
def read(index):
    # added print line to display indexed item to user
    print(checklist[index])
    return checklist[index]

# updates item in list
def update(index, item):
    checklist[index] = item

# deletes item from list
def destroy(index):
    checklist.pop(index)

# adds checkmark to item
def mark_completed(index):
    checklist[index] = ("{} {}".format("√", checklist[index]))

# takes user input   
def user_input(prompt):
    user_input = input(prompt).lower()
    return user_input

# selection based on user input
def select(function_code):
    if function_code == "c":
        input_item = user_input(f"{Green}Input item: {reset}")
        create(input_item)

    elif function_code == "r":
        item_index = user_input(f"{Green}Index Number?: {reset}")
        read(int(item_index))

    elif function_code == "p":
        list_all_items()

    elif function_code == "u":
        update_item = user_input(f"{Green}Index number?: {reset}")
        replace_item_with = user_input(f"{Green}Enter in new item: {reset}")
        update(int(update_item), replace_item_with)

    elif function_code == "d":
        destroy_item = user_input(f"{Green}Index Number?: {reset}")
        destroy(int(destroy_item))

    elif function_code == "z":
        check_item = user_input(f"{Green}Index number?: {reset}")
        mark_completed(int(check_item))

    elif function_code == "q":
        exit()
    else:
        pass

    # keeps loop running
    return True

running = True
while running:
    selection = user_input(f"c adds to the list, u replaces an item, d deletes an item, r reads from it, p displays the list, q exits the loop, \n Enter here:")
    running = select(selection)
    if user_input not in ['c', 'u', 'd', 'r', 'p', 'q']:
        print(f"{Yellow}Not an option{reset}")
    else:
        os.system('clear')

