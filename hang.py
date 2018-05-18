#! /usr/bin/python
import time
import logging
from os import system
from Classes.word import Word
from Classes.hangman import Hangman

logging.basicConfig(filename='hang.log', format='%(asctime)s %(message)s', level=logging.DEBUG)
WORDLIST_FILENAME = "words.txt"

def checkTypeOfVariable(variable, correctType):
    if type(variable) != correctType:
        print 'In hang.py'
        print 'Incorrect type of variable. Function cant work properly. Exiting...'
        logging.error('Variable is in INCORRECT type')
        exit(1)
    else:
        logging.info('Variable is in correct type')

def printLoadSituation(lenWordlist = int):
    checkTypeOfVariable(lenWordlist, int)
    print 'Loading word list from file... Wait a few seconds, please'
    time.sleep(2)
    print lenWordlist, 'words loaded.'
    option = str(raw_input('Press \033[91mENTER\033[0m to start... '))
    option = validateOption(option)


def validateOption(option = str):
    checkTypeOfVariable(option, str)
    while option != '':
        print 'Invalid character. Try again'
        option = str(raw_input('Press \033[91mENTER\033[0m to start... '))
    return str(option)

def printWelcomeMessage(secretWord = str, numberDifferentLetters = int):
    checkTypeOfVariable(secretWord, str)
    checkTypeOfVariable(numberDifferentLetters, int)
    system("clear")
    print '\033[91mWelcome to the game, Hangman!\033[0m'
    print '\033[91mI am thinking of a word that is\033[33m', len(secretWord),'\033[0m\033[91mletters long.\033[0m'
    print '\033[91mThe word has\033[33m', numberDifferentLetters,'\033[0m\033[91mdifferent letters.\033[0m'
    print '-------------'
    print 'Lets get started...'
    print '\033[91m3\033[0m'
    time.sleep(1)
    print '\033[33m2\033[0m'
    time.sleep(1)
    print '1'

def main():
    word = Word(WORDLIST_FILENAME)
    word.openArchive()
    word.readArchive()
    word.makeListOfWords()
    word.calculateLengthOfWordlist()
    printLoadSituation(word.length)
    word.chooseWord()
    word.calculateDifferentLetters()
    while word.chooseAnotherWord() == 1:
        word.chooseWord()
        word.calculateDifferentLetters()
    printWelcomeMessage(word.secretWord, word.numberDifferentLetters)
    game = Hangman(word.getSecretWord())
    game.hangman()

if __name__ == "__main__":
    main()
