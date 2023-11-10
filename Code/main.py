import copy
import random
import sys


# function to turn create dictionary for items
def item_details_to_dict(index: int = None, name: str = None, brand: str = None, price: float = None, quantity: int = None, category: str = None,  purch_date: str = None):
    dict = {
        "item_code": index,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity,
        "category": category,
        "purch_date": purch_date
    }

    return dict

# function to add item dictionary to inventory list
def add_item_details(dict: dict, item_list:list):
    item_list.append(dict)

# function to find item from inventory list by index
def find_by_index(index:int, item_list:list):
    for i in item_list:
        if i.get("item_code") == index:
            return i


# function to update item details in the inventory by searching through the index
def update_item_details(index: int, dict: dict, item_list: list):
    exist_dict = find_by_index(index, item_list)
    exist_dict_index = item_list.index(exist_dict)

    for val1, val2 in zip(exist_dict, dict):
        if dict[val2] == None or dict[val2] == 0:
            dict[val2] = exist_dict[val1]

    item_list[exist_dict_index] = dict


def delete_item_details(item_code: int, item_list:list):
    list_length_before = len(item_list)

    if list_length_before > 0:
        index = item_list.index(find_by_index(item_code, item_list))
        if index < list_length_before:
            item_list.pop(index)

    if list_length_before > len(item_list):
        print("Item Deleted Successfully")

def view_item_details(item_list:list):
    order_list = sorted(item_list, key= lambda x: x["category"], reverse=False)

    for i in order_list:
        print('-' * 30)
        for key, val in i.items():
            print(key.ljust(12, ' '), " | ", str(val).ljust(12, ' '))
        print()

def save_to_file(item_list:list, file_path:str):
    with open(file_path, 'w') as file:
        for i in item_list:
            for x,y in i.items():
                file.write((str(x) + ":" + str(y) + "\n"))
            file.write("\n")

def read_dealers_from_file(file_path):
    temp_list = []
    dealer_list = []
    try:
        with open(file_path, "r") as file:
            # read file line by line
            for line in file:
                temp_list.append(line)
    except FileNotFoundError:
        print("Dealer List File Not Found!")


    temp_dict = {
        "dealer_name": "",
        "contact_no": "",
        "location": "",
        "items": []
    }

    for i in temp_list:

        element_list = i.rstrip("\n").split(":")

        if element_list[0] == "dealer_name":
            temp_dict["dealer_name"] = element_list[1]
        if element_list[0] == "contact_no":
            temp_dict["contact_no"] = element_list[1]
        if element_list[0] == "location":
            temp_dict["location"] = element_list[1]

        item_list = i.rstrip("\n").split(",")

        if len(item_list) > 1:
            items_dict = {"name": item_list[0],
                          "brand": item_list[1],
                          "price": item_list[2],
                          "quantity": item_list[3]
                          }
            temp_dict["items"].append(items_dict)

        if i == "\n" or temp_list.index(i) == len(temp_list) - 1:
            dealer_list.append(copy.copy(temp_dict))
            temp_dict['items'] = []
            continue



    return dealer_list


def select_random_dealers():
    dealer_list = read_dealers_from_file(dealer_list_file_path)
    chosen_dealer_list = random.sample(dealer_list, 4)
    return chosen_dealer_list


def sort_random_dealers_by_location(chosen_dealer_list: list):
    sorted_dealer_list = sorted(chosen_dealer_list, key= lambda x: x["location"], reverse=False)
    return sorted_dealer_list

def view_dealer_list(dealer_list: list, dealer_name: str= None):

    for i in dealer_list:
        if dealer_name != None:
            if i['dealer_name'].lower().strip(" ") != dealer_name.lower().strip(" "):
                continue
        print("*" * 30)
        for key, val in i.items():
            if type(val) == list:
                print("Items List\n")
                for j in val:
                    print("-" * 30)
                    for key1, val1 in j.items():
                        print(key1.ljust(12, ' '), " | ", val1.ljust(12, ' '))
                    print()
            else:
                print(key.ljust(12, ' '), " | ", val.ljust(12, ' '))



def float_validation(prompt="Enter Float: "):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def int_validation(prompt="Enter Integer: "):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def string_validation(prompt="Enter String: "):
    while True:
        value = input(prompt)
        if value.isalpha() or " " in value or value == 0:
            return value
        else:
            print("Invalid input. Please enter a valid string.")

def naming_validation(prompt="Enter Name: "):
    while True:
        value = input(prompt)
        if value != None or value != "" or value == 0:
            return value
        else:
            print("Invalid input. Please enter a valid string.")

def date_string_validation(prompt="Enter Date: "):
    while True:
        value = input(prompt).replace('/', " ").replace(".", " ").replace("-", " ").split()
        if (len(value[0]) == 4 and len(value[1]) == 2 and len(value[2]) == 2) or value == 0:
            return value
        else:
            print("Invalid Input. Please enter a valid string")




item_list = []
item_list_file_path = 'item_list.txt'
dealer_list_file_path = 'dealer_list.txt'
sorted_dealers = None
print("Inventory Management".center(50, "-"))


while True:

    user_input = input("Choose Input\n\nType AID for adding item details\nType DID for deleting item details\nType UID for updating item details\nType VID for viewing the items table. (Sort according to the items category) and print the current total\nType SID for saving the item details to the text file at any time\nType SDD for selecting four dealers randomly from a file\nType VRL for displaying all the details of the randomly selected dealers. (Sorted according to the location)\nType LDI for display the items of the given dealer\nType ESC to exit the program\n\n").upper()

    if user_input == None or user_input == "":
        continue

    if user_input == "AID":
        index = int_validation("Enter Item Code: ")
        item_name = string_validation("Enter Item Name: ")
        brand = naming_validation("Enter Brand Name: ")
        price = float_validation("Enter Price: ")
        quantity = int_validation("Enter Quantity: ")
        category = string_validation("Enter Item Category: ")
        purch_date = date_string_validation("Enter Date: ")

        item_details_dict = item_details_to_dict(index, item_name, brand, price, quantity, category, purch_date)
        add_item_details(item_details_dict, item_list)
        print()

    elif user_input == "DID":
        index = int_validation("Enter Index of The Item You Want To Delete: ")
        delete_item_details(index, item_list)
        print()

    elif user_input == "UID":
        index = int_validation("Enter Item Code of The Item You Want To Update: ")
        item_name = string_validation("Enter Item Name: ")
        brand = naming_validation("Enter Brand Name: ")
        price = float_validation("Enter Price: ")
        quantity = int_validation("Enter Quantity: ")
        category = string_validation("Enter Item Category: ")
        purch_date = date_string_validation("Enter Date: ")

        item_details_dict = item_details_to_dict(index, item_name, brand, price, quantity, category, purch_date)
        update_item_details(index, item_details_dict, item_list)

    elif user_input == "VID":
        #item list sorted according to item category as mentioned on 2nd page in the CW spec sheet. But on the 3rd page in the table it says to sort it in descending order accroding to item id
        view_item_details(item_list)
        print()

    elif user_input == "SID":
        save_to_file(item_list, item_list_file_path)
        print()

    elif user_input == "SDD":
        random_dealers = select_random_dealers()
        sorted_dealers = sort_random_dealers_by_location(random_dealers)
        print("4 Dealers are selected randomly")

    elif user_input == "VRL":
        if sorted_dealers == None:
            random_dealers = select_random_dealers()
            sorted_dealers = sort_random_dealers_by_location(random_dealers)

        view_dealer_list(sorted_dealers)

    elif user_input == "LDI":
        dealer_name = string_validation("Enter Dealer Name: ")

        view_dealer_list(sorted_dealers, dealer_name)

    elif user_input == "ESC":
        sys.exit()

    else:
        print("Wrong Input")

