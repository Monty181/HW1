from pyisemail import is_email
from tabulate import tabulate


class Contact:

    def __init__(self, name, phone, email):
        self.contact_name = name
        self.contact_phone = phone
        self.contact_email = email

    def get_name(self):
        return self.contact_name

    def get_phone(self):
        return self.contact_phone

    def get_email(self):
        return self.contact_email

    def get_contact(self):
        return [self.contact_name, self.contact_phone, self.contact_email]


class ContactBook:
    contact_list = []

    def add_contact(self, contact_item):
        self.contact_list.append(contact_item)

    def print_book(self):
        table = []
        for i in self.contact_list:
            table.append(Contact.get_contact(i))
        return table

    def find_name(self, search_word):
        table = []
        for i in self.contact_list:
            if search_by_name == Contact.get_name(i):
                table.append(Contact.get_contact(i))
        return table

    def find_number(self, search_number):
        table = []
        for i in self.contact_list:
            if search_by_phone == Contact.get_phone(i):
                table.append(Contact.get_contact(i))
        return table

    def delete_contact(self, name):
        for i, j in enumerate(self.contact_list):
            if delete_contact_name == Contact.get_name(j):
                self.contact_list.pop(i)
                return True


class Validator:

    @staticmethod
    def check_email(email):
        return is_email(email)

    @staticmethod
    def check_name(name):
        return len(name) > 2


menu = ("""
1. Add contact
2. Find contact
3. Print all
4. Delete contact
5. Exit
""")
contact_book = ContactBook()
choice = -1

while choice != 5:
    print(menu)
    choice = int(input("Please input action number: "))
    if choice == 1:
        contact_name = str(input("Please enter contact name: "))
        while not Validator.check_name(contact_name):
            print("Name is too small")
            contact_name = str(input("Please enter contact name: "))
        contact_phone = str(input("Please enter contact phone number: "))
        contact_email = str(input("Please enter contact email: "))
        while not Validator.check_email(contact_email):
            print("Email is invalid")
            contact_email = str(input("Please enter contact email: "))
        contact = Contact(contact_name, contact_phone, contact_email)
        contact_book.add_contact(contact)
        print("New contact has been added")

    elif choice == 2:
        search_choice = int(input("""
        1. Search by contact name
        2. Search by phone number

        Please enter search action number: """))
        if search_choice == 1:
            search_by_name = str(input("Please enter contact name: "))
            print(tabulate(contact_book.find_name(search_by_name), headers=["Name", "Phone", "Email"]))
        elif search_choice == 2:
            search_by_phone = str(input("Please enter contact phone number: "))
            contact_book.find_number(search_by_phone)
            print(tabulate(contact_book.find_number(search_by_phone), headers=["Name", "Phone", "Email"]))

    elif choice == 3:
        print(tabulate(contact_book.print_book(), headers=["Name", "Phone", "Email"]))

    elif choice == 4:
        delete_contact_name = str(input("Please enter contact name that you want to delete: "))
        if contact_book.delete_contact(delete_contact_name):
            print("Contact was removed successfully")

    elif choice == 5:
        print("Bye!")
        break

    else:
        print("You input wrong action number")

