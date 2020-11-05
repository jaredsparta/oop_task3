# Creates a dictionary that stores each letter and its value
list1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
list2 = ["D", "G"]
list3 = ["B", "C", "M", "P"]
list4 = ["F", "H", "V", "W", "Y"]
list5 = ["K"]
list8 = ["J", "X"]
list10 = ["Q", "Z"]

letters_to_points = {}

for letter in list1:
    letters_to_points[letter] = 1
for letter in list2:
    letters_to_points[letter] = 2
for letter in list3:
    letters_to_points[letter] = 3
for letter in list4:
    letters_to_points[letter] = 4
for letter in list5:
    letters_to_points[letter] = 5
for letter in list8:
    letters_to_points[letter] = 8
for letter in list10:
    letters_to_points[letter] = 10

#####

class Values:
    def __init__(self, word):
        self.word = word.upper
        self.score(self.word)

    
    def score(self, word):
        pass