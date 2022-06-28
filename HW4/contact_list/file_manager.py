import pickle


class FileManager:

    @staticmethod
    def open_file(book_path):
        try:
            with open(book_path, "rb") as file:
                res = pickle.load(file)
            return res
        except FileNotFoundError:
            print("Something went wrong. Your file wasn't found")

    @staticmethod
    def write_file(book_path, book_final_list):
        with open(book_path, "wb") as file:
            pickle.dump(book_final_list, file)




