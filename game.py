from methods import *

class Game:
    def __init__(self, n):
        self.length = n
        self.pWords = get_words(n)
        self.words = self.pWords.copy()
        #TODO self.letters = 
        self. history = []
        self.won = False

    def updateGame(self, guess, pattern):
        self.history.append((guess, pattern))
        # TODO remove all words from pWords that don't match the pattern

    def game_won(self, solution):
        """congratulates the player and saves the solution"""
        self.solution = solution
        self.won = True
        print("Du hast das Wort erraten!")

    def showHistory(self):
        #TODO
        a = 1
        
    def getPossWords(self):
        return self.pWords


    #TODO def entropy(self, g , pWords):

    #TODO def sortGuesses(self, strict):


