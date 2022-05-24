
menu = ("""
1. Add contact
2. Find contact
3. Print all
4. Exit
""")
print(menu)
choice = int(input("Please input action number: "))
contact_list = {}

while choice != 4:

    if choice == 1:
        contact_name = str(input("Please enter contact name: "))
        phone_number = int(input("Please enter contact phone number: "))
        contact_item = {contact_name: phone_number}
        contact_list = contact_list | contact_item
        print("New contact has been added")
        print(menu)
        choice = int(input("Please input action number: "))

    elif choice == 2:
        search_choice = int(input("""
        1. Search by contact name
        2. Search by phone number
        
        Please enter search action number: """))
        if search_choice == 1:
            search_by_name = str(input("Please enter contact name: "))
            if search_by_name in contact_list.keys():
                print(f"{search_by_name} - {contact_list[search_by_name]}")
        elif search_choice == 2:
            search_by_phone = int(input("Please enter contact phone number: "))
            for key, value in contact_list.items():
                if search_by_phone == value:
                    print(f"{key} - {value}")

        print(menu)
        choice = int(input("Please input action number: "))


    elif choice == 3:
        for i in contact_list.items():
            print(*i)
        print(menu)
        choice = int(input("Please input action number: "))

    elif choice == 4:
        break

    else:
        print("You input wrong action number")
        print(menu)
        choice = int(input("Please input action number: "))
