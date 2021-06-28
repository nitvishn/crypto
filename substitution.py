from copy import copy
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


def substitute(plaintext, mapping):
    ciphertext = ""
    for char in plaintext:
        if char.lower() == char:
            ciphertext += char
        elif char.lower() in mapping:
            ciphertext += mapping[char.lower()]
        else:
            ciphertext += char.upper()
    return ciphertext


def loadWords(wordfile):
    global dictionary
    dictionary = set()
    file = open(wordfile, 'r')
    for line in file:
        dictionary.add(line.replace('\n', ''))


def frequencies(sentence):
    freqdict = {}
    for alpha in alphabet:
        freqdict[alpha] = 0
    for char in sentence:
        if char in alphabet:
            freqdict[char] += 1 / len(sentence)
    return freqdict


def sortWithFrequencies(freqdict, add_frequencies=False):
    L = list(freqdict.keys())
    L.sort(reverse=True, key=lambda x: freqdict[x])
    if add_frequencies:
        for i in range(len(L)):
            L[i] = (L[i], freqdict[L[i]])
    return L


def bestScore(word):
    def getScore(word, entry):
        matching = 0
        if len(word) != len(entry):
            return 0
        for i in range(len(word)):
            if word[i] == entry[i]:
                matching += 1
        return matching / len(word)

    if word in dictionary:
        return 1
    bestScore = 0
    for entry in dictionary:
        bestScore = max(bestScore, getScore(word, entry))
    return bestScore


def score(sentence):
    forbidden_chars = ['!', '?']
    for char in forbidden_chars:
        sentence.replace(char, '')
    tot = 0
    for word in sentence.split():
        tot += bestScore(word)
    return tot


def most_occuring_doubles(ciphertext):
    occurances = {}
    for i in range(0, len(ciphertext) - 2, 2):
        if ciphertext[i] != ciphertext[i + 1]:
            continue
        string = ciphertext[i:i + 2]
        occurances[string] = occurances.get(string, 0) + 1
    return occurances


def most_occuring_string(ciphertext, length, same_char=False):
    occurances = {}
    for i in range(0, len(ciphertext) - length, length):
        string = ciphertext[i:i + length]
        if ' ' in string:
            continue
        occurances[string] = occurances.get(string, 0) + 1
    return occurances


def most_occuring_words(ciphertext, wordlength):
    words = ciphertext.split(' ')
    occurances = {}
    for word in words:
        if len(word) == wordlength:
            occurances[word] = occurances.get(word, 0) + 1
    return occurances


def randomMapping(samemap=[]):
    keys = alphabet
    for alpha in samemap:
        keys.remove(alpha)
    values = copy(keys)
    random.shuffle(values)
    freqdict = {}
    for i in range(len(alphabet)):
        freqdict[alphabet[i]] = values[i]
    return freqdict


def printAnalysis(ciphertext):
    freqdict = frequencies(ciphertext)
    print("Order Frequency of Characters:")
    print(sortWithFrequencies(freqdict))
    print("\nOrder Frequency of Digraphs:")
    print(sortWithFrequencies(most_occuring_string(ciphertext, 2)))
    print("\nOrder Frequency of Trigraphs:")
    print(sortWithFrequencies(most_occuring_string(ciphertext, 3)))
    print("\nOrder Frequency of Doubles:")
    print(sortWithFrequencies(most_occuring_doubles(ciphertext)))
    print("\nOrder Frequency of Two-Letter Words")
    print(sortWithFrequencies(most_occuring_words(ciphertext, 2)))
    print("\nOrder Frequency of Three-Letter Words")
    print(sortWithFrequencies(most_occuring_words(ciphertext, 3)))


def inputAndRandomScramble():
    plaintext = input("Plaintext: ")
    print("Ciphertext:", substitute(plaintext, randomMapping(' ')))

def inputStringFromFile(filename):
    file = open(filename, 'r')
    string = file.read()
    return string

def writeStringToFile(string, filename):
    file = open(filename, 'w')
    file.write(string)

# inputAndRandomScramble()
loadWords('words.txt')
# ciphertext = "TLMOYQ JQC GULCMNTVTN MLFHlLTVQRlT, HLEMl ELT PUlTC VTFTQlTN MEC JTQkLTCCTC"

mapping = randomMapping(samemap = ['v', 'b', ' '])
mapping['v'] = 'b'
mapping['b'] = 'v'

print(mapping)

while True:
    text = input("plain: ")
    print('cipher:', substitute(text, mapping))

print(mapping)
# printAnalysis(ciphertext)
# ciphertext = substitute(ciphertext, mapping)
#
# print('\n' + ciphertext)
