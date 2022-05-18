#function to count the number of words in a text
def count_words(text):
    return len(text.split())
    
number_of_words = count_words("Hello World, My name is Python")
print(number_of_words)