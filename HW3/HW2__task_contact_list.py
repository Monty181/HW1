class Contacts:

    contact_list = {}

    def __init__(self, name, phone):
        self.contact_name = name
        self.contact_phone = phone
        self.contact_list[self.contact_name] = self.contact_phone
        print("New contact has been added")


menu = ("""
1. Add contact
2. Find contact
3. Print all
4. Exit
""")

contact_list = {}
choice = -1

while choice != 4:
    print(menu)
    choice = int(input("Please input action number: "))
    if choice == 1:
        contact_name = str(input("Please enter contact name: "))
        contact_phone = str(input("Please enter contact phone number: "))
        contact = Contacts(contact_name, contact_phone)

    elif choice == 2:
        search_choice = int(input("""
        1. Search by contact name
        2. Search by phone number
        
        Please enter search action number: """))
        if search_choice == 1:
            search_by_name = str(input("Please enter contact name: "))
            if search_by_name in Contacts.contact_list.keys():
                print(f"{search_by_name} - {Contacts.contact_list[search_by_name]}")
        elif search_choice == 2:
            search_by_phone = str(input("Please enter contact phone number: "))
            for key, value in Contacts.contact_list.items():
                if search_by_phone == value:
                    print(f"{key} - {value}")

    elif choice == 3:
        print(Contacts.contact_list)

    elif choice == 4:
        print("Bye!")
        break

    else:
        print("You input wrong action number")
