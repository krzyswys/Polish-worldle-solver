from __future__ import unicode_literals
import codecs


def countUniq(word):
    c = 0
    for letter in word:
        if (
            letter == "a"
            or letter == "c"
            or letter == "o"
            or letter == "u"
            or letter == "i"
            or letter == "y"
            or letter == "e"
        ):
            c += 1
    return c


def countSpec(word):
    c = 0
    for letter in word:
        if (
            letter == "ą"
            or letter == "ć"
            or letter == "ó"
            or letter == "ź"
            or letter == "ż"
            or letter == "ł"
            or letter == "ę"
            or letter == "ś"
        ):
            c += 1
    return c


# -*- coding: utf-8 -*-


def getWordList():
    wordlList = []
    with codecs.open("dic.txt", "r", "utf-8") as f:
        for line in f:
            word = line.strip()
            if len(word) == 5:
                wordEl = []
                wordEl.append(countUniq(word))
                wordEl.append(countSpec(word))
                wordEl.append(word)
                wordlList.append(wordEl)
    return wordlList


def getWordListWithout(letter, wordList):
    newWordList = []
    for el in wordList:
        if letter not in el[2]:
            newWordList.append(el)
    return newWordList


def getWordListWithLetterInDiffrentPlace(letter, index, wordList):
    newWordList = []
    for el in wordList:
        if letter in el[2] and el[2][index] != letter:
            newWordList.append(el)
    return newWordList


def getWordListWith(letter, wordList):
    newWordList = []
    for el in wordList:
        if letter in el[2]:
            newWordList.append(el)
    return newWordList


def wordNotExists(el, wordList):
    wordList.remove(el)
    return wordList


def sortByUniq(wordlist):
    return sorted(wordlist, key=lambda x: x[0], reverse=True)


def getWordListWithLettersAtIndexes(f, s, t, fr, fh, wordList):
    newWordList = []
    for el in wordList:
        c = 0
        if f != "-":
            if el[2][0] == f:
                c += 1
        else:
            c += 1
        if s != "-":
            if el[2][1] == s:
                c += 1
        else:
            c += 1
        if t != "-":
            if el[2][2] == t:
                c += 1
        else:
            c += 1
        if fr != "-":
            if el[2][3] == fr:
                c += 1
        else:
            c += 1
        if fh != "-":
            if el[2][4] == fh:
                c += 1
        else:
            c += 1
        if c == 5:
            newWordList.append(el)
    return newWordList


def getWordListWithoutLettersAtIndexes(f, s, t, fr, fh, wordList):
    newWordList = []
    for el in wordList:
        c = 0
        if f != "-":
            if el[2][0] != f:
                c += 1
        else:
            c += 1
        if s != "-":
            if el[2][1] != s:
                c += 1
        else:
            c += 1
        if t != "-":
            if el[2][2] != t:
                c += 1
        else:
            c += 1
        if fr != "-":
            if el[2][3] != fr:
                c += 1
        else:
            c += 1
        if fh != "-":
            if el[2][4] != fh:
                c += 1
        else:
            c += 1
        if c == 5:
            newWordList.append(el)
    return newWordList


wordList = getWordList()
wordList = sortByUniq(wordList)
wordList = getWordListWithout("i", wordList)
wordList = getWordListWithout("e", wordList)
wordList = getWordListWithLetterInDiffrentPlace("o", 0, wordList)
wordList = getWordListWithLetterInDiffrentPlace("c", 1, wordList)
wordList = getWordListWithLetterInDiffrentPlace("c", 1, wordList)
wordList = getWordListWithLetterInDiffrentPlace("o", 4, wordList)
wordList = getWordListWithLettersAtIndexes("c", "-", "-", "-", "-", wordList)
wordList = getWordListWithout("k", wordList)


# wordList = wordNotExists(wordList[0], wordList)
# wordList = wordNotExists(wordList[0], wordList)
# wordList = wordNotExists(wordList[0], wordList)
# wordList = getWordListWithout("g", wordList)
# wordList = getWordListWithout("u", wordList)
# wordList = getWordListWithLettersAtIndexes("-", "u", "-", "-", "-", wordList)
# wordList = getWordListWithLetterInDiffrentPlace("a", 0, wordList)
# wordList = getWordListWithLetterInDiffrentPlace("r", 4, wordList)


print(wordList[0])

for el in wordList:
    if el[2] == "bułka":
        print("asda")
# for el in getWordListWithout("a", getWordList()):
#     print(el)
