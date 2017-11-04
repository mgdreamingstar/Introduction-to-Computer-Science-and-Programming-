# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "D:\Github\Introduction-to-Computer-Science-and-Programming-\Problem_Set_6\words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    # >>> isWord(wordList, 'bat') returns
    True
    # >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("D:\Github\Introduction-to-Computer-Science-and-Programming-\Problem_Set_6\story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    assert 0 <= shift <= 26
    before_up = string.ascii_uppercase
    before_low = string.ascii_lowercase
    after_up = []
    after_low = []
    for letter in before_up:
        ind = (before_up.index(letter) + shift) % 26
        after_up.append(before_up[ind])
    for letter in before_low:
        ind = (before_low.index(letter) + shift) % 26
        after_low.append(before_low[ind])

    before = before_up + before_low
    after = after_up + after_low

    dict_out = dict(zip(before,after))
    return dict_out

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    out = []
    for letter in text:
        if letter in string.ascii_uppercase or letter in string.ascii_lowercase:
            out.append(coder[letter])
        else:
            out.append(letter)

    return ''.join(out)

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### HINT: This is a wrapper function.
    coder = buildCoder(shift)
    return applyCoder(text, coder)

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """

    """
    my pseudo code:
    1. try with shift = 1 to 25
    2. split words with space
    3. check if every words is in wordlist
    4. store the grade this shifted sentence gets
    5. find the max grade
    """
    shift = 0
    max_valid = 0
    best_shift = 0
    while shift <= 26:
        valid_word = 0
        text_origin = applyShift(text, shift)
        words_list = text_origin.split(' ')

        for word in words_list:
            if isWord(wordList, word):
                valid_word += 1

        if valid_word > max_valid:
            max_valid = valid_word
            best_shift = shift
        shift += 1
    return best_shift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    story = getStoryString()
    shift = findBestShift(wordList, story)
    return applyShift(story, shift)

def decryptStory_new(story):
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    shift = findBestShift(wordList, story)
    return applyShift(story, shift)
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
    print decryptStory_new('Nonsense words: ticket relief from full marry abroad offend pinch first reproduction matter cool outside cave spite straight religion pool sign moderate safety hour whatever spare idea book log surround hasten cross favorite director manner preference relation')
    print decryptStory_new('Cdchtcht ldgsh: ixrzti gtaxtu ugdb ujaa bpggn pqgdps duutcs excrw uxghi gtegdsjrixdc bpiitg rdda djihxst rpkt hexit higpxvwi gtaxvxdc edda hxvc bdstgpit hputin wdjg lwpitktg hepgt xstp qddz adv hjggdjcs wphitc rgdhh upkdgxit sxgtridg bpcctg egtutgtcrt gtapixdc')
    print decryptStory()
    findBestShift(wordList, 'Uryyb, jbeYQ!')
    findBestShift(wordList, 'Dro aEsJ sC... rkbn!')
    applyShift('Dro aEsJ sC... rkbn!', 16)
    story = getStoryString()
    findBestShift(wordList, story)
    applyShift(story, 16)
