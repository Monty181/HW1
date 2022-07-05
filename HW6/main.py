import app
from file_manager import FileManager
import sys
import parser_module


def main():

    parser = parser_module.ParserApp.create_parser()
    args = parser.parse_args()

    if "-pt" in sys.argv:
        path_text = args.path_text
    else:
        path_text = str(input("Hello, please enter path for the file with text: "))
    if "-bw" in sys.argv:
        path_bad_words = args.path_bad_words
    else:
        path_bad_words = str(input("Please enter path for file with bad words: "))
    if "-cf" in sys.argv:
        path_censored_file = args.path_censored_file
    else:
        path_censored_file = str(input("Please enter path you want to save censored file: "))

    censor_analyzer = app.CensorAnalyzer(FileManager.open_file(path_text), FileManager.open_file(path_bad_words))
    FileManager.write_file(path_censored_file, censor_analyzer.remove_bad_words())
    censor_analyzer.print_console_count_bad_words()


if __name__ == '__main__':
    main()

