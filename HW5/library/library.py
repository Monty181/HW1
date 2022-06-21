import book


class Library:

    def __init__(self):
        self.library_catalog = []

    def add_book(self, new_book):
        self.library_catalog.append(new_book)

    def find_book_by_title(self, key_word):
        search_result = []
        for i in self.library_catalog:
            if key_word == book.Book.get_title(i):
                search_result.append(book.Book.get_book(i))
        return search_result

    def find_book_by_author(self, key_word):
        search_result = []
        for i in self.library_catalog:
            if key_word == book.Book.get_author(i):
                search_result.append(book.Book.get_book(i))
        return search_result

    def find_book_by_publishing_house(self, key_word):
        search_result = []
        for i in self.library_catalog:
            if key_word == book.Book.get_publishing_house(i):
                search_result.append(book.Book.get_book(i))
        return search_result

    def find_book_by_language(self, key_word):
        search_result = []
        for i in self.library_catalog:
            if key_word == book.Book.get_language(i):
                search_result.append(book.Book.get_book(i))
        return search_result

    def print_library_catalog(self):
        library_table = []
        for i in self.library_catalog:
            library_table.append(book.Book.get_book(i))
        return library_table


