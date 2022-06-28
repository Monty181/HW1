import contact_module


class ContactBook:

    def __init__(self):
        self.contact_list = []

    def add_contact(self, contact_item):
        self.contact_list.append(contact_item)

    def print_book(self):
        table = []
        for i in self.contact_list:
            table.append(contact_module.Contact.get_contact(i))
        return table

    def find_name(self, search_word):
        table = []
        for i in self.contact_list:
            if search_word == contact_module.Contact.get_name(i):
                table.append(contact_module.Contact.get_contact(i))
        return table

    def find_number(self, search_number):
        table = []
        for i in self.contact_list:
            if search_number == contact_module.Contact.get_phone(i):
                table.append(contact_module.Contact.get_contact(i))
        return table

    def delete_contact(self, delete_contact_name):
        for i, j in enumerate(self.contact_list):
            if delete_contact_name == contact_module.Contact.get_name(j):
                self.contact_list.pop(i)
                return True

    def get_contacts_from_file(self, res1):
        for i in res1:
            contact = contact_module.Contact(i[0], i[1], i[2])
            self.add_contact(contact)

    def prepare_for_saving_to_file(self):
        table = []
        for i in self.contact_list:
            table.append(contact_module.Contact.get_contact(i))
        return table

