class FileManager:

    @staticmethod
    def open_file(path):
        try:
            with open(path, "r") as f:
                res = list(f.read().split(" "))
            return res
        except FileNotFoundError:
            print("Something went wrong. Your file wasn't found")

    @staticmethod
    def write_file(path, words_list):
        with open(path, "w") as f:
            f.write(" ".join(words_list))



