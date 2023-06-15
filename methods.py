def get_words(n):
    """Reads a file and returns a list of all words of length n in it
       all words are in lower case and have no linebreak at the end"""
    
    letters = set("abcdefghijklmnopqrstuvwxyzßäöü")

    words = []  #TODO numpy array might be faster
    with open("allWords.txt", "r") as file:
        for line in file:
            line = line.strip()
            if len(line) == n:
                line = line.lower()
                if all(e in letters for e in line): # check if line only contains allowed letters
                    words.append(line)
    return words

