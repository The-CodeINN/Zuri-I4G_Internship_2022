# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string

alphabet_string_u = string.ascii_uppercase
alphabet_string_u = list(alphabet_string_u)
alphabet_string_l = string.ascii_lowercase
alphabet_string_l = list(alphabet_string_l)
all_letters = alphabet_string_u + alphabet_string_l


def read_file_content(filename):
    with open(filename) as fhandle:
        file = fhandle.readlines()
        words_only = []
        for sentences in file:
            sentence = sentences.split()
            for words in sentence:
                if words[len(words)-1] in all_letters:
                    words_only.append(words)
                else:
                    nice_letters = words.replace(words[len(words)-1], "")
                    words_only.append(nice_letters)
    return words_only

def count_words():
    
    my_dict = {}
    text = read_file_content("./story.txt")
    for word in text:
        if word in my_dict:
            my_dict[word] += 1
            
        else:
            my_dict[word] = 0
            my_dict[word] += 1
    return my_dict

print(count_words())
