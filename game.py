import random
from string import ascii_lowercase

from methods import *

class Game:
    def __init__(self, n):
        self.length = n
        self.pWords = get_words(n)
        self.words = self.pWords.copy()
        self.letters = self.create_letters()
        self.history = []
        self.won = False

    def updateGame(self, guess, pattern):
        self.history.append((guess, pattern))
        if all(e == "2" for e in pattern):
            self.game_won(guess)
            return
        # removes all words from pWords that don't match the pattern
        for e in self.pWords:
            if get_pattern(guess, e) != pattern:
                self.pWords.remove(e)

    def game_won(self, solution):
        """congratulates the player and saves the solution"""
        clear_screen()
        self.solution = solution
        self.won = True
        print("Du hast das Wort erraten!")
        print("Das Wort war:" + "\033[1;32m", solution + "\033[0m")
    
        
    def getPossWords(self):
        return self.pWords


    def entropy(self, g , pWords):
        #TODO implement entropy
        return random.randint(1,1000)

    def sortGuesses(self, strict):
        sorted_list = []
        if strict:
            sorted_list = sorted (self.pWords , key = lambda a : a[1])
        else:
            sorted_list = sorted(self.words, key=lambda a: a[1])
        return sorted_list
    
    def showHistory(self):
        clear_screen()
        for guess, pattern in self.history:
            print(color_word(pattern, guess))

        print()

        for i in ascii_lowercase + "äöüß":
            print(self.color_letter(i) + i + "\033[0m", end=" ")
        print("\n")

    def showHints(self, pWords, sortedList):
        five_words = []
        lowest_ent = 100000
        for word in pWords:
            ent = self.entropy(word,pWords)
            if ent < lowest_ent:
                lowest_ent = ent
                five_words.append(word)
                if len(five_words) == 5:
                    break

        for word in five_words:
            print(word)

        if len(pWords) <= 100:
            for word in pWords:
                print(word)
        return 0

    def create_letters(self):
        """creates a dictionary with letters as keys and 0 as value"""
        letters = {}
        [letters.update({x : 0}) for x in ascii_lowercase+"äöüß"]
        return letters
    
    def color_letter(self, letter):
        """returns the color of a letter
           white:  no information
           red:    letter is not in the solution
           yellow: we know the letter is in the solution, but not the position
           green:  we know the letter is in the solution and the position"""
        
        white = "\033[0m"
        yellow = "\033[1;33m"
        green = "\033[1;32m"
        red = "\033[1;31m"

        # [i for i, x in enumerate(e) if x == letter] #all indices where the letter occurs in the word e 
        
        for e in self.history:
            for i in range(len(e[0])):
                if e[0][i] == letter and e[1][i] == "2":
                    return green
        
        for e in self.history:
            for i in range(len(e[0])):
                if e[0][i] == letter and e[1][i] == "1":
                    return yellow
        
        if all([not letter in e[0] for e in self.history]):
            return white
            
        return red

            