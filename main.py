# Cedric Krug
# cedric.krug@uni-konstanz.de

# Natascha Schulz
# natascha.schulz@uni-konstanz.de

# Zimo Yang
# zimo.yang@uni-konstanz.de



#%% Run this first
import os

from methods import *

white = "\033[0m"
yellow = "\033[1;33m"
green = "\033[1;32m"



#%%
def get_pattern(v, w):
    """matching pattern of v (guess) in w (solution) according to wordle rules"""
    pattern = [0] * len(v)

    # check for correct letters at correct positions
    for i in range(len(v)):
        if v[i] == w[i]:
            pattern[i] = 2

    # check for correct letters at wrong positions
    # (only if letter is not already marked as correct)
    for i in range(len(v)):
        if v[i] != w[i] and occurences_till_now(v, pattern, i) <= occurences_in_solution(v[i], w, pattern):
            pattern[i] = 1

    return ''.join([str(x) for x in pattern])
                
#%%
def occurences_till_now(v, pattern, i):
    """returns the number of occurences of v[i] in v[0..i]
       excluding correct letters at correct positions"""
    count = 0
    for j in range(i+1):
        if v[j] == v[i] and pattern[j] != 2:
            count += 1
    return count
    
#%%
def occurences_in_solution(letter, solution, pattern):
    """returns the number of occurences of letter in solution
       excluding correct letters at correct positions"""
    count = 0
    for i in range(len(solution)):
        if solution[i] == letter and pattern[i] != 2:
            count += 1
    return count

#%%
def color_word(pattern, word):
    """returns a colored version of word according to pattern
       0 -> white
       1 -> yellow
       2 -> green"""
    colored_word = ""
    for i in range(len(pattern)):
        if pattern[i] == "0":
            colored_word += word[i]
        elif pattern[i] == "1":
            colored_word += yellow + word[i] + white
        elif pattern[i] == "2":
            colored_word += green + word[i] + white
    return colored_word + white

#%%
def clear_screen():
    """clears the terminal, works on windows, macOS and Linux"""
    os.system('cls' if os.name == 'nt' else 'clear')

#%%
def check_manual_mode():
    """asks the user if he wants to play in manual mode"""
    while True:
        mode = input("Do you want to play in manual mode? (y/n): ")
        if mode == "y":
            return True
        elif mode == "n":
            return False
        else:
            print("Please enter y or n.")

#%%
def play_manual_mode():
    """plays the game in manual mode"""
    guesses = 0
    while guesses < 10:
        guess = input("Wort: ")
        if guess == solution:
            solved()
            return
        else:
            if len(guess) != len(solution):
                print("Das Wort hat", len(solution), "Buchstaben, du hast aber", len(guess), "Buchstaben eingegeben.")
                continue
            
            validity = valid_word(guess, words)
            if validity == 0:
                pass
            elif validity == 1:
                print("Bitte gib ein Wort ein, das nur aus Buchstaben besteht.")
                continue
            else: #validity == 2
                print("Das Wort existiert nicht. Bitte versuche es erneut.")
                continue

            print("Player 1: please enter the pattern for the word Player 2 just entered")
            pattern = input("Pattern: ")
            if len(pattern) != len(solution):
                print("The pattern has to have the same length as the solution.")
                continue

            if not valid_pattern(pattern):
                print("The pattern can only contain 0, 1 and 2.")
                continue

            clear_screen()
            print(color_word(pattern, guess))
            guesses += 1
    print("Du hast das Wort nicht erraten. Das Wort war:", solution)

#%%
def play_auto_mode():
    """plays the game in auto mode"""
    guesses = 0
    while guesses < 10: 
        guess = input("Wort: ")
        if guess == solution:
            solved()
            return
        else:
            if len(guess) != len(solution):
                print("Das Wort hat", len(solution), "Buchstaben, du hast aber", len(guess), "Buchstaben eingegeben.")
                continue
            validity = valid_word(guess, words)
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
    print("Du hast das Wort nicht erraten. Das Wort war:", solution)


#%%
def solved():
    """congratuates the player for solving the word"""
    print("Du hast das Wort erraten!")

#%%
def valid_word(word, words):
    """checks if word only contains letters and is contained in allWords.txt
       0 -> valid word
       1 -> not only letters
       2 -> not in allWords.txt"""
    
    letters = set("abcdefghijklmnopqrstuvwxyzßäöü")
    if all(e in letters for e in word):
        if word in words:   #TODO: words are sorted, binary search is possible.
            return 0
        return 2    
    else: 
        return 1

#%%
def valid_pattern(pattern):
    """checks if pattern only contains 0, 1 and 2"""
    return all(e in "012" for e in pattern)


#%%
clear_screen()
manual = check_manual_mode()

print("Spieler 1: Bitte gib ein Wort ein, das der andere Spieler erraten soll.")
while True:
    solution = input("Wort: ")
    words = get_words(len(solution))

    validity = valid_word(solution, words)
    if validity == 0:
        clear_screen()
        break
    elif validity == 1:
        print("Bitte gib ein Wort ein, das nur aus Buchstaben besteht.")
        continue
    else: #validity == 2
        print("Das Wort existiert nicht. Bitte versuche es erneut.")
        continue


print("Spieler 2: Du hast 10 Versuche, um das Wort zu erraten. Das Wort hat", len(solution), "Buchstaben.")

if not manual:
    play_auto_mode()
else:
    play_manual_mode()

