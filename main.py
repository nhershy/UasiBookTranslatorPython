import os
import string

import en_core_web_trf

nlp = en_core_web_trf.load()

global g_future
global g_past
global g_conditional
global g_negation
global g_remove_word
global g_uasi_word

# ----------------------- Functions ------------------------------

def auxilaryWordCheck(token, next_token):
    global g_remove_word
    global g_conditional
    global g_future
    global g_past
    global g_negation

    # list of words to pass
    if token.text.lower() == "may":
        pass
    elif token.pos_ == "AUX":
        if next_token.pos_ != "ADJ" and next_token.pos_ != "ADV" and next_token.pos_ != "PRON":
            g_remove_word = True
        if token.text.lower() == "would":
            g_conditional = True
        elif token.text.lower() == "will":
            g_future = True
        if "Tense=Past" in token.morph:
            g_past = True
    elif token.pos_ == "PART":
        if "Polarity=Neg" in token.morph:
            g_remove_word = True
            g_negation = True

def resetGlobalVariables():
    global g_future
    global g_past
    global g_conditional
    global g_negation
    global g_remove_word
    global g_uasi_word

    g_future = False
    g_past = False
    g_conditional = False
    g_negation = False
    g_remove_word = False
    g_uasi_word = ""

def endOfSentenceReset(token):
    if token.is_sent_end:
        resetGlobalVariables()
        return True
    else:
        return False

def isIrregularUasiWord(token):
    global g_uasi_word

    word = ""
    special_words = ['me', 'she', 'he', 'we']

    if token.text.lower() in special_words:
        word = token.text.lower()
    else:
        word = token.lemma_.lower()

    if word == "me":
        g_uasi_word = "ma"
    elif word == "she":
        g_uasi_word = "sha"
    elif word == "he":
        g_uasi_word = "ha"
    elif word == "we":
        g_uasi_word = "wa"
    elif word == "be":
        g_uasi_word = "ba"
    elif word == "do":
        g_uasi_word = "da"
    elif word == "to":
        g_uasi_word = "ta"
    elif word == "a":
        g_uasi_word = "ikaku"
    elif word == "an":
        g_uasi_word = "ikaku"
    elif word == "the":
        g_uasi_word = "osi"
    elif word == "what":
        g_uasi_word = "ako"
    elif word == "and":
        g_uasi_word = "upa"
    elif word == "for":
        g_uasi_word = "fosi"
    elif word == "if":
        g_uasi_word = "opho"
    elif word == "but":
        g_uasi_word = "wula"
    elif word == "at":
        g_uasi_word = "anoc"
    elif word == "on":
        g_uasi_word = "oin"
    elif word == "in":
        g_uasi_word = "oin"

def ifWordEndsInW():
    global g_uasi_word

    if g_uasi_word.endswith('w') and not isProperNoun(token):
        g_uasi_word = g_uasi_word[:-1] + "v"

def primeForDoubleVowelShift(word):
    if "ee" in word:
        return word.replace("ee", "ii")
    elif "oo" in word:
        return word.replace("oo", "uu")
    return word

def performVowelShift(token, last_token):
    global g_uasi_word

    if isProperNoun(token):
        g_uasi_word = token.text

    # if uasi_word == "" at this stage, that means that it is not an irregular noun, so continue doing vowel shift
    elif g_uasi_word == "":
        word = ""
        # If prevoius word is have/has/had
        if last_token.lemma_.lower() == "have" and "Tense=Past" in token.morph and "VerbForm=Part" in token.morph:
            word = token.lemma_.lower()
        # If Verb is Past Participle
        elif "Tense=Past" in token.morph and "VerbForm=Part" in token.morph:
            word = token.text.lower()
        else:
            word = token.lemma_.lower()
        word = primeForDoubleVowelShift(word)
        vowel_shifted_word = ""
        for c in word:
            if c == 'a':
                vowel_shifted_word += 'e'
            elif c == 'e':
                vowel_shifted_word += 'i'
            elif c == 'i':
                vowel_shifted_word += 'o'
            elif c == 'o':
                vowel_shifted_word += 'u'
            elif c == 'u':
                vowel_shifted_word += 'a'
            elif c == 'y':
                vowel_shifted_word += 'S'
            else:
                vowel_shifted_word += c

        g_uasi_word = vowel_shifted_word

def addOrisSonos(token, next_token, last_token):
    global g_uasi_word
    global g_future
    global g_conditional
    global g_past
    global g_negation

    # If Verb and Past Participle acting like adjective/noun, don't add Oris Sonos
    # Unless If is Verb and Past Participle, and word that preceeded it was "have"
    if "Tense=Past" in token.morph and "VerbForm=Part" in token.morph and last_token.lemma_.lower() != "have":
        return

    # If Verb
    if token.pos_ == "VERB" or (token.pos_ == "AUX" and next_token.pos_ == "ADJ"):
        # Past tense = L
        if "Tense=Past" in token.morph or g_past:
            g_uasi_word += 'L'
            g_past = False
            g_conditional = False
        # Future tense = P
        elif g_future:
            g_uasi_word += 'P'
            g_future = False
            g_conditional = False
        # Conditional tense = H
        elif g_conditional:
            g_uasi_word += 'H'
            g_conditional = False

        if g_negation:
            g_uasi_word += 'X'
            g_negation = False

    # Else, if Noun
    # Plurality = T
    if token.pos_ == "NOUN":
        if "Number=Plur" in token.morph:
            g_uasi_word += 'T'

def createUasiString(uasi_word_list):

    uasi_string = ""
    for word in uasi_word_list:
        if len(word) == 1 and any(p in word for p in string.punctuation):
            uasi_string = (uasi_string[:-1] + word + " ")
        else:
            uasi_string = (uasi_string + word + " ")

    return uasi_string

def isProperNoun(token):
    if token.pos_ == "PROPN":
        return True
    return False

def endWithPunctuation(input):
    if input != "":
        last_char = input[-1]
        if not any(p in last_char for p in string.punctuation):
            return input + "."

def createUniversalFilePath(relative_pathname):
    base_dir = os.path.dirname(__file__)
    return os.path.join(base_dir, relative_pathname)

def loadBook(relative_path):
    contents = ""
    absolute_path = createUniversalFilePath(relative_path)
    with open(absolute_path) as f:
        contents = f.read()
    return contents

def showProgress(count, total):
    if (count % 10000 == 0):
        print("{0}%".format(int((count / total) * 100)))

# ----------------------- Main ------------------------------

# Initialize globals
g_future = False
g_past = False
g_conditional = False
g_negation = False
g_remove_word = False
g_uasi_word = ""

FILE_PATH = "the_godfather.txt"
DEBUG = False

uasi_word_list = []
input = ""

if DEBUG:
    input = "The men who had tried to dishonour her"
    input = endWithPunctuation(input)
else:
    print("(1/3) Importing File...")
    input = loadBook(FILE_PATH)

print("(2/3) Tokenizing Words...")
tokens = nlp(input)

total_count = len(tokens)
print("(3/3) Uasizing Words...")
print("Total Words: {0}".format(total_count))
index = -1
count = 0
for token in tokens:
    index += 1

    count += 1
    showProgress(count, total_count)

    if endOfSentenceReset(token):
        uasi_word_list.append(token.text)
        continue

    auxilaryWordCheck(token, tokens[index+1])

    if g_remove_word:
        g_remove_word = False
        continue

    isIrregularUasiWord(token)

    isProperNoun(token)

    # If not an irregular Uasi word
    performVowelShift(token, tokens[index-1])

    ifWordEndsInW()

    addOrisSonos(token, tokens[index+1], tokens[index-1])

    uasi_word_list.append(g_uasi_word)
    g_uasi_word = ""

if DEBUG:
    print(input)
    uasi_string = createUasiString(uasi_word_list)
    print(uasi_string)
else:
    with open('result.txt', 'w') as f:
        f.write(createUasiString(uasi_word_list))
        print("Uasi Conversion Complete!")

# ------------------------ Notes -------------------------

#use spacy model "for accuracy"
#https://spacy.io/models

# Open in file
# Read data in memory
# Tokenize words
# Lemmatize words
# Remove auxilary verbs
# Remove negation words (no, not, don't, etc)
# Check if word is irregular word (1 of 16)
## if yes, substitute word for irregular
## if not, perform vowel shift (and also change "y" to "S")
# if word ends in "w", replace with "v"
# Add Oris Sonos:
## (skip if verb is past participle)
## if negative polarity before verb, add X
## elif word is plural, add T
## elif word is past tense, add L
## elif word is future tense, add P
## elif word is conditionatl tense, add H
# Remove gerunds (if verb is present continuous, "aspect=prog", just use lemma)