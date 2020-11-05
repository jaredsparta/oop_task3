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

class Value:
    def __init__(self):
        self.past_words = []

    
    def score(self, word):
        score = 0
        for letter in word.upper():
            score += letters_to_points[letter]
        return score

    
    def add_word(self, word):
        score = self.score(word)
        self.past_words.append(f"{word} : {score} points")

    
    def check_past_words(self):
        for words in self.past_words:
            print(words)


game = Value()

while True:
    choice = input("""\nWhat would you like to do?
                1. Find the value of a word
                2. Check all words that you've typed
                3. Exit
                        """)

    if choice == "1":
        word = input("\nWhat word?")
        game.add_word(word)
        print(game.score(word))

    if choice == "2":
        game.check_past_words()

    if choice == "3":
        break
