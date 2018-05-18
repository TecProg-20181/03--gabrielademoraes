import string
import random
import logging
from os import system

class Word():
    def __init__(self, fileName = str):
        self.checkTypeOfVariable(fileName, str)
        self.__fileName = str(fileName)
        self.__inFile = file
        self.__line = str
        self.__wordlist = list
        self.length = int
        self.secretWord = str
        self.numberDifferentLetters = int
        self.__option = str

    def checkTypeOfVariable(self, variable, correctType):
        if type(variable) != correctType:
            print 'In word.py'
            print 'Incorrect type of variable. Function cant work properly. Exiting...'
            logging.error('Variable is in INCORRECT type')
            exit(1)
        else:
            logging.info('Variable is in correct type')

    def openArchive(self):
        try:
            self.__inFile = open(self.__fileName, 'r', 0)
            self.checkTypeOfVariable(self.__inFile, file)
            logging.info('Opening archive success')
        except IOError:
            print 'Opening archive fail... File doesnt exist'
            logging.error('Opening archive fail... File doesnt exist')
            exit(2)

    def readArchive(self):
        self.__line = str(self.__inFile.readline())
        self.checkTypeOfVariable(self.__line, str)

    def makeListOfWords(self):
        self.__wordlist = list(string.split(self.__line))
        self.checkTypeOfVariable(self.__wordlist, list)
        self.__inFile.close()

    def calculateLengthOfWordlist(self):
        self.length = int(len(self.__wordlist))
        self.checkTypeOfVariable(self.length, int)

    def chooseWord(self):
        self.secretWord = str(random.choice(self.__wordlist).lower())
        self.checkTypeOfVariable(self.secretWord, str)

    def calculateDifferentLetters(self):
        differentLetters = set(self.secretWord)
        self.checkTypeOfVariable(differentLetters, set)

        self.numberDifferentLetters = int(len(differentLetters))
        self.checkTypeOfVariable(self.numberDifferentLetters, int)

    def chooseAnotherWord(self):
        guesses = 8
        if guesses < self.numberDifferentLetters:
            system("clear")
            print '\033[33mWARNING!\033[0m'
            print 'In the word drawn'
            print 'The number of different letters is higher than the number of guesses'
            print '\033[92mIf you would like to change, sometimes you will have to press yes more than once until the system draw a word that fits\033[0m'
            self.__option = str(raw_input('Do you want to change the word ? [y/n] '))
            self.validateOption()
            if self.__option == 'y':
                return int(1)

    def validateOption(self):
        self.checkTypeOfVariable(self.__option, str)
        while self.__option != 'y' and self.__option != 'n':
            print 'Invalid character! Try again'
            self.__option = str(raw_input('Do you want to change the word ? [y/n] '))

    def getSecretWord(self):
        return str(self.secretWord)
