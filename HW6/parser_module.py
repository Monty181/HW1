import argparse


class ParserApp:

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument("-pt", dest="path_text", help="Path for file with text")
        parser.add_argument("-bw", dest="path_bad_words", help="Path for file with bad words")
        parser.add_argument("-cf", dest="path_censored_file", help="Path you want to save censored file")
        return parser

