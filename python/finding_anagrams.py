# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # Remove spacing in word and anagram
    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")

    # Check if word and anagram characters are same
    if sorted(word.lower()) == sorted(anagram.lower()):
        return True

    else:
        return False


print(find_anagram("hello", "mello"))
print(find_anagram("Below", "elbow"))
print(find_anagram("anagram", "Nag a ram"))
# nagaram
