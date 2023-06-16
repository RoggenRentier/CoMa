from string import ascii_lowercase

from methods import *

class Game:
    def __init__(self, n):
        self.length = n
        self.pWords = get_words(n)
        self.words = self.pWords.copy()
        self.letters = self.create_letters()
        self. history = []
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
        self.solution = solution
        self.won = True
        print("Du hast das Wort erraten!")

    #TODO def showHistory(self):
    
        
    def getPossWords(self):
        return self.pWords


    #TODO def entropy(self, g , pWords):

    #TODO def sortGuesses(self, strict):



    def create_letters(self):
        """creates a dictionary with letters as keys and 0 as value"""
        letters = {}
        [letters.update({x : 0}) for x in ascii_lowercase+"äöüß"]
        return letters
