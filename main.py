# Cedric Krug
# cedric.krug@uni-konstanz.de

# Natascha Schulz
# natascha.schulz@uni-konstanz.de

# Zimo Yang
# zimo.yang@uni-konstanz.de



#%% Run this first
import os
import random

from methods import *
from game import Game

global game


#%%
def play_manual_mode():
    """plays the game in manual mode"""

    global game

    guesses = 0
    while guesses < game.length + 1 and not game.won:
        guess = input("Wort: ").lower()

        #check if the guess is valid
        if len(guess) != len(solution):
            print("Das Wort hat", len(solution), "Buchstaben, du hast aber", len(guess), "Buchstaben eingegeben.")
            continue
        
        validity = valid_word(guess, game.words)
        if validity == 0:
            pass
        elif validity == 1:
            print("Bitte gib ein Wort ein, das nur aus Buchstaben besteht.")
            continue
        else: #validity == 2
            print("Das Wort existiert nicht. Bitte versuche es erneut.")
            continue

        #check if the pattern is valid
        print("Player 1: please enter the pattern for the word Player 2 just entered")
        while True:
            pattern = input("Pattern: ")

            if len(pattern) != len(solution):
                print("The pattern has to have the same length as the solution.")
                continue

            if not valid_pattern(pattern):
                print("The pattern can only contain 0, 1 and 2.")
                continue

            break

        clear_screen()
        print(color_word(pattern, guess))
        guesses += 1

        game.updateGame(guess, pattern)


    if not game.won:
        print("Du hast das Wort nicht erraten. Das Wort war:", solution)




#%%
def play_auto_mode():
    """plays the game in auto mode"""

    global game

    guesses = 0
    while guesses < game.length + 1 and not game.won: 
        guess = input("Wort: ").lower()
        
        #check if the guess is valid
        if len(guess) != len(solution):
            print("Das Wort hat", len(solution), "Buchstaben, du hast aber", len(guess), "Buchstaben eingegeben.")
            continue
        validity = valid_word(guess, game.words)
        if validity == 0:
            pass
        elif validity == 1:
            print("Bitte gib ein Wort ein, das nur aus Buchstaben besteht.")
            continue
        else: #validity == 2
            print("Das Wort existiert nicht. Bitte versuche es erneut.")
            continue
            

        print(color_word(get_pattern(guess, solution), guess))
        guesses += 1

        game.updateGame(guess, get_pattern(guess, solution))


    if not game.won:
        print("Du hast das Wort nicht erraten. Das Wort war:", solution)


#%%
def check_mode():
    """asks the user which mode he wants to play
       0: manual mode
       1: 2 player auto mode
       2: 1 player auto mode"""
    while True:
        print("In which mode do you want to play?")
        print("0: manual mode")
        print("1: 2 player auto mode")
        print("2: 1 player auto mode")
        mode = input("mode: ")
        if mode not in ["0", "1", "2"]:
            print("Please enter 0, 1 or 2.")
            continue
        else:
            return int(mode)


#%%
def init_solution_2player():
    """asks the user for the solution word"""

    global game

    print("Spieler 1: Bitte gib ein Wort ein, das der andere Spieler erraten soll.")
    while True:
        solution = input("Wort: ").lower()
        #words = get_words(len(solution))
        game = Game(len(solution))

        validity = valid_word(solution, game.words)
        if validity == 0:
            clear_screen()
            return solution
        elif validity == 1:
            print("Bitte gib ein Wort ein, das nur aus Buchstaben besteht.")
            continue
        else: #validity == 2
            print("Das Wort existiert nicht. Bitte versuche es erneut.")
            continue


def init_solution_1player():
    """program generates a number from 5-25 (probability based on word length distribution), 
    program chooses a random word with that length"""
    global game

    #number of words with length n: 5-25
    my_weights = [6784, 13604, 25455, 48472, 84671, 128381, 165226, 187985, 190164, 181289, 167661, 148211, 128337, 106668, 85571, 66373, 49748, 36560, 25984, 18292, 12694]
    n = random.choices(range(5, 26), weights=my_weights)[0]

    game = Game(n)
    return random.choice(game.words)
    

#%%
def clear_screen():
    """clears the terminal, works on windows, macOS and Linux"""
    os.system('cls' if os.name == 'nt' else 'clear')






#%% Main Program

clear_screen()

mode = check_mode()

clear_screen()

if mode < 2:
    solution = init_solution_2player()
    print("Spieler 2: Du hast", game.length+1, "Versuche, um das Wort zu erraten. Das Wort hat", game.length, "Buchstaben.")
else:
    solution = init_solution_1player()
    print("Du hast", game.length+1, "Versuche, um das Wort zu erraten. Das Wort hat", game.length, "Buchstaben.")


if mode == 0:
    play_manual_mode()
else:
    play_auto_mode()
    

