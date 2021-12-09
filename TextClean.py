Myfile = open("cerpen.txt", "r", encoding='utf-8')
#my text is named input.txt 
#'r' along with file name depicts that we want to read it
string_of_words = ""
for x in Myfile:
    a_string = x;
    alphanumeric = ""
    for character in a_string:
        if character.isalnum() or character == " ":
            alphanumeric += character
    string_of_words += alphanumeric

list_string_of_words = string_of_words.split()

