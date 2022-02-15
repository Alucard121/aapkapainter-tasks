# Write a code that prints out the first occurrence of a duplicate in a given array of integers


word1 = input("first word:").lower()
word2 = input("second word:").lower()

def check(first_word, second_word):
    if len(first_word) == len(second_word) and set(first_word) == set(second_word):
        print("the given strings are anagram")
    else:
        print("the given strings are not anagram")


check(first_word=word1, second_word=word2)