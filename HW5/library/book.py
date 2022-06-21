class Book:

    def __init__(self, author, title, publishing_house, language):
        self.author = author
        self.title = title
        self.publishing_house = publishing_house
        self.language = language

    def get_author(self):
        return self.author

    def get_title(self):
        return self.title

    def get_publishing_house(self):
        return self.publishing_house

    def get_language(self):
        return self.language

    def get_book(self):
        return [self.author, self.title, self.publishing_house, self.language]

    def __str__(self):
        return f'Short overview: This is a book "{self.title}" that was written by {self.author} and was published by {self.publishing_house} in {self.language}'

