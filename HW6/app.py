class CensorAnalyzer:

    def __init__(self, res1, res2):
        self.res1 = res1
        self.res2 = res2

    def remove_bad_words(self):
        result_list = []
        for i in self.res1:
            if i in self.res2:
                continue
            else:
                result_list.append(i)
        return result_list

    def count_bad_words(self):
        bad_count_words_result = {}
        for i in self.res2:
            bad_count_words_result[i] = self.res1.count(i)
        return bad_count_words_result

    def print_console_count_bad_words(self):
        print("Founded bad words: ")
        for i in self.count_bad_words():
            print(f"{i} - {self.count_bad_words()[i]} times")

