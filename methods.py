#%%

import os

white = "\033[0m"
yellow = "\033[1;33m"
green = "\033[1;32m"



#%%
def get_words(n):
    """Reads a file and returns a list of all words of length n in it
       all words are in lower case and have no linebreak at the end"""
    
    letters = set("abcdefghijklmnopqrstuvwxyzßäöü")

    words = []
    with open("allWords.txt", "r") as file:
        for line in file:
            line = line.strip()
            if len(line) == n:
                line = line.lower()
                if all(e in letters for e in line): # check if line only contains allowed letters
                    words.append(line)
    return words

#%%
def valid_pattern(pattern):
    """checks if pattern only contains 0, 1 and 2"""
    return all(e in "012" for e in pattern)

#%%
def valid_word(word, words):
    """checks if word only contains letters and is contained in allWords.txt
       0 -> valid word
       1 -> not only letters
       2 -> not in allWords.txt"""
    
    letters = set("abcdefghijklmnopqrstuvwxyzßäöü")
    if all(e in letters for e in word):
        if word in words:
            return 0
        return 2    
    else: 
        return 1
    

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

#%% just for testing
def print_file(filename, words):
    """prints all words in words to filename"""
    with open(filename, "w") as file:
        for word in words:
            file.write(word + "\n")