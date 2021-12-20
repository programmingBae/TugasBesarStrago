from Stopwords import stopword_list
'''
--Source--
cerpenmu.com
'''

class TextClean:
    def __init__(self, filename):
        self.filename = filename
        self.string_of_words = ""
        self.list_string_of_words = []
        self.list_string_without_stopwords = []
        self.open_file(self.filename)

    def open_file(self, filename):
        Myfile = open(filename, "r", encoding='utf-8')
        string_of_words = ""
        for x in Myfile:
            a_string = x;
            alphanumeric = ""
            for character in a_string:
                if character.isalnum() or character == " ":
                    alphanumeric += character
            string_of_words += alphanumeric

        list_string_of_words = string_of_words.split()
        list_string_without_stopwords = [word for word in list_string_of_words if word not in stopword_list]
        self.string_of_words = string_of_words
        self.list_string_of_words = list_string_of_words
        self.list_string_without_stopwords = list_string_without_stopwords

    def get_string_of_words(self):
        return self.string_of_words

    def get_list_string_of_words(self):
        return self.list_string_of_words

    def get_list_string_without_stopwords(self):
        return self.list_string_without_stopwords





