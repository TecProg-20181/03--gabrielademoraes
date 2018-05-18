import string
import logging
from os import system

class Hangman:
    def __init__(self, secretWord = str):
        self.secretWord = str(secretWord)
        self.lettersGuessed = []

    def checkTypeOfVariable(self, variable, correctType):
        if type(variable) != correctType:
            print 'In hangman.py'
            print 'Incorrect type of variable. Function cant work properly. Exiting...'
            logging.error('Variable is in INCORRECT type')
            exit(1)
        else:
            logging.info('Variable is in correct type')

    def isWordGuessed(self):
        self.checkTypeOfVariable(self.secretWord, str)
        self.checkTypeOfVariable(self.lettersGuessed, list)
        letter = str
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False
        return True


    def getGuessedWord(self, string = str):
        self.checkTypeOfVariable(string, str)
        guessed = str('')
        letter = str
        self.checkTypeOfVariable(self.secretWord, str)
        self.checkTypeOfVariable(self.lettersGuessed, list)
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                guessed += letter
            else:
                guessed += ' _ '
        print string, guessed
        print '====================================================================='

    def getAvailableLetters(self):
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase
        return str(available)

    def processLettersAvailable(self):
        available = self.getAvailableLetters()
        self.checkTypeOfVariable(available, str)
        letter = str
        for letter in available:
            if letter in self.lettersGuessed:
                available = available.replace(letter, '')
        return str(available)

    def printResult(self):
        system("clear")
        self.checkTypeOfVariable(self.isWordGuessed(), bool)
        if self.isWordGuessed() == True:
            print '==========================================='
            print '\033[92mCongratulations, you won! =)\033[0m '
            print 'The word was \033[45m', self.secretWord, '\033[0m.'
            print '==========================================='
        else:
            print '====================================================================='
            print '\033[92mSorry, you ran out of guesses =(\033[0m'
            print 'The word was \033[45m', self.secretWord, '\033[0m.'
            print '===================================================================='

    def validateLetterInput(self, letter = str):
        while letter.isalpha() == False or len(letter) != 1:
            print 'Please insert only letters'
            letter = str(raw_input('\033[32mPlease guess a letter:\033[0m '))
        return str(letter.lower())

    def hangman(self):
        guesses = int(8)
        self.checkTypeOfVariable(self.isWordGuessed(), bool)

        while  self.isWordGuessed() == False and guesses > 0:
            print 'You have ', guesses, 'guesses left.'

            available = str(self.processLettersAvailable())
            print 'Available letters\033[33m', available,'\033[0m'

            letter = str(raw_input('\033[32mPlease guess a letter:\033[0m '))
            letter = self.validateLetterInput(letter)

            if letter in self.lettersGuessed:
                string = str('\033[32mOops! You have already guessed that letter:\033[0m ')
                self.getGuessedWord(string)

            elif letter in self.secretWord:
                self.lettersGuessed.append(letter)
                string = '\033[32mGood Guess:\033[0m '

                self.getGuessedWord(string)

            else:
                guesses -=1
                self.lettersGuessed.append(letter)
                string = str('\033[32mOops! That letter is not in my word:\033[0m ')

                self.getGuessedWord(string)

        else:
            self.printResult()
