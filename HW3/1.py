from pyisemail import is_email
from tabulate import tabulate
import phonenumbers


class Contacts:
    contact_list = []

    def __init__(self, name, phone, email):
        self.contact_name = name
        self.contact_phone = phone
        self.contact_email = email
        self.contact_list.append(self)
        print("New contact has been added")

    def get_name(self):
        return self.contact_name

    def get_phone(self):
        return self.contact_phone

    def get_contact(self):
        return [self.contact_name, self.contact_phone, self.contact_email]

    @staticmethod
    def check_email(email):
        return is_email(email)

    @staticmethod
    def check_name(name):
        return len(name) > 2

    # @staticmethod
    # def check_phone(str_phone):
    #     phone = phonenumbers.parse(str_phone)
    #     return phonenumbers.is_possible_number(phone)



menu = ("""
1. Add contact
2. Find contact
3. Print all
4. Delete contact
5. Exit
""")

choice = -1

while choice != 5:
    print(menu)
    choice = int(input("Please input action number: "))
    if choice == 1:
        contact_name = str(input("Please enter contact name: "))
        while not Contacts.check_name(contact_name):
            print("Name is too small")
            contact_name = str(input("Please enter contact name: "))
        contact_phone = str(input("Please enter contact phone number: "))
        # while not Contacts.check_phone(contact_phone):
        #     print("Phone number is invalid")
        #     contact_phone = str(input("Please enter contact phone number: "))
        contact_email = str(input("Please enter contact email: "))
        while not Contacts.check_email(contact_email):
            print("Email is invalid")
            contact_email = str(input("Please enter contact email: "))
        contact = Contacts(contact_name, contact_phone, contact_email)

    elif choice == 2:
        search_choice = int(input("""
        1. Search by contact name
        2. Search by phone number

        Please enter search action number: """))
        if search_choice == 1:
            search_by_name = str(input("Please enter contact name: "))
            for i in Contacts.contact_list:
                if search_by_name == Contacts.get_name(i):
                    print(Contacts.get_contact(i))
        elif search_choice == 2:
            search_by_phone = str(input("Please enter contact phone number: "))
            for i in Contacts.contact_list:
                if search_by_phone == Contacts.get_phone(i):
                    print(Contacts.get_contact(i))

    elif choice == 3:
        table = []
        for i in Contacts.contact_list:
            table.append(Contacts.get_contact(i))
        print(tabulate(table, headers=["Name", "Phone", "Email"]))

    elif choice == 4:
        delete_contact_name = str(input("Please enter contact name that you want to delete: "))
        for i, j in enumerate(Contacts.contact_list):
            if delete_contact_name == Contacts.get_name(j):
                Contacts.contact_list.pop(i)
                print("Contact was removed successfully")

    elif choice == 5:
        print("Bye!")
        break

    else:
        print("You input wrong action number")
