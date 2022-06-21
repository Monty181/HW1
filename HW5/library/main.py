from tabulate import tabulate
import library


def main():

    menu = """
    1. Add new book
    2. See all books
    3. Find book
    4. Exit
    """

    my_library = library.Library()
    action_number = 0
    print("Hello, it is your library!")

    while action_number != 4:
        print(menu)
        action_number = int(input("Please choose number of the action you want to do: "))
        if action_number == 1:
            input_author = str(input("Enter the author of the book: "))
            input_title = str(input("Enter title of the book: "))
            input_publishing_house = str(input("Enter the publishing house of the book: "))
            input_language = str(input("Enter language of the book: "))
            new_book = library.book.Book(input_author, input_title, input_publishing_house, input_language)
            my_library.add_book(new_book)
            print("Your book was added to the library successfully")
        elif action_number == 2:
            print(tabulate(my_library.print_library_catalog(),
                           headers=['Author', 'Title', 'Publishing house', 'Language']))
        elif action_number == 3:
            print("""
            1. Search by author
            2. Search by book title
            3. Search by publishing house
            4. Search by book language
            """)
            search_action_number = int(input("Choose number of search you want to use: "))
            if search_action_number == 1:
                search_key = str(input("Enter book author you want to find: "))
                print(tabulate(my_library.find_book_by_author(search_key),
                               headers=['Author', 'Title', 'Publishing house', 'Language']))
            elif search_action_number == 2:
                search_key = str(input("Enter book title you want to find: "))
                print(tabulate(my_library.find_book_by_title(search_key),
                               headers=['Author', 'Title', 'Publishing house', 'Language']))
            elif search_action_number == 3:
                search_key = str(input("Enter publishing house that books you want to find: "))
                print(tabulate(my_library.find_book_by_publishing_house(search_key),
                               headers=['Author', 'Title', 'Publishing house', 'Language']))
            elif search_action_number == 4:
                search_key = str(input("Enter language of the book you want to find: "))
                print(tabulate(my_library.find_book_by_language(search_key),
                               headers=['Author', 'Title', 'Publishing house', 'Language']))
            else:
                print("Please enter correct search number")
        elif action_number == 4:
            print("Bye, see you later!")
            break
        else:
            print("Please enter right action number")


if __name__ == '__main__':
    main()









