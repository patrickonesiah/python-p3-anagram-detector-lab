# your code goes here!

class Anagram:

    def __init__ (self, word):
        self.word = word

    def match(self, listOfWords):
        newList = []

        for word in listOfWords:
            letterList = [letter for letter in word]
            if sorted(letterList) == sorted(self.word):
                newList.append(word)
                
        return newList

# Better solution
# class Anagram:
#     def __init__(self, word):
#         self.word_letters = sorted([letter for letter in word])

#     def match(self, word_list):
#         match_word_list = []

#         for word in word_list:
#             if sorted([letter for letter in word]) == self.word_letters:
#                 match_word_list.append(word)

#         return match_word_list