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
