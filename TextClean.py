from Stopwords import stopword_list
'''
--Source--
cerpenmu.com
'''
Myfile = open("cerpen.txt", "r", encoding='utf-8')
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



