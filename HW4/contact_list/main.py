from tabulate import tabulate
import contact_module
import contact_book_module
import validator_module
import file_manager


def main():
    menu = ("""
    1. Add contact
    2. Find contact
    3. Print all
    4. Delete contact
    5. Exit
    """)
    contact_book = contact_book_module.ContactBook()
    book_path = "contact_book_db.txt"
    contact_book.get_contacts_from_file(file_manager.FileManager.open_file(book_path))

    choice = -1

    while choice != 5:
        print(menu)
        choice = int(input("Please input action number: "))
        if choice == 1:
            contact_name = str(input("Please enter contact name: "))
            while not validator_module.Validator.check_name(contact_name):
                print("Name is too small")
                contact_name = str(input("Please enter contact name: "))
            contact_phone = str(input("Please enter contact phone number: "))
            contact_email = str(input("Please enter contact email: "))
            while not validator_module.Validator.check_email(contact_email):
                print("Email is invalid")
                contact_email = str(input("Please enter contact email: "))
            contact = contact_module.Contact(contact_name, contact_phone, contact_email)
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
            file_manager.FileManager.write_file(book_path, contact_book.prepare_for_saving_to_file())
            break

        else:
            print("You input wrong action number")


if __name__ == '__main__':
    main()

