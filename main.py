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
    # Every instance keeps track of past words checked
    def __init__(self):
        self.past_words = []

    # Returns the score of a word
    def score(self, word):
        score = 0
        for letter in word.upper():
            score += letters_to_points[letter]
        return score

    # Adds a word to the past words attribute
    def add_word(self, word):
        score = self.score(word)
        self.past_words.append(f"{word} : {score} points")

    # Prints each word in the past words attribute
    def check_past_words(self):
        if not self.past_words:
            print("\nYou haven't checked any words yet!")
        for words in self.past_words:
            print(words)

# Initialises the class to use
game = Value()

# The loop continues until the user decides to stop
while True:
    # The user has 3 choices on what to do
    choice = input("""\nWhat would you like to do?
                1. Find the value of a word
                2. Check all words that you've typed
                3. Exit
                       -> """)

    # If they choose to check the score of a word this happens
    # The if statement checks if they inputted ONLY letters
    # Otherwise the word is valid and it adds it to the past words
    # and displays the score
    if choice == "1":
        word = input("\nWhat word? ")
        if not word.isalpha():
            print("Only letters allowed!")
            continue
        game.add_word(word)
        print(f"{word} has a score of {game.score(word)}")

    # This just lists the words the user has inputted already
    if choice == "2":
        game.check_past_words()

    # This exits the loop
    if choice == "3":
        break
