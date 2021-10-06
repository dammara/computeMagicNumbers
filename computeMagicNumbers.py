# Markhus Dammar
# 6 October 2021
# This program will find the magic number of any word inputted by the user, then find the sum of the digits in the magic number

wordToNumberList = []


def getEquivalentNumber(_myChar):
    for letter in lowercase_conversion:
        corresponding_number = (ord(letter))-96
        wordToNumberList.append(corresponding_number)


def computeSumOfCharacters(myWord):
    sumOfCharacters = sum(wordToNumberList)
    #print(f"The magic number of '{user_word}' is: " + str(sumOfCharacters))
    return sumOfCharacters


def computeSumOfDigits(myNumber):
    sumOfDigits = sum(map(int, str(myNumber)))
    print(f"The sum of the digits (magic number) of '{user_word}' is {sumOfDigits}")


user_word = input("Please enter a word: ")
lowercase_conversion = user_word.lower()
getEquivalentNumber(lowercase_conversion)
sumOfDigits_global = computeSumOfCharacters(lowercase_conversion)
computeSumOfDigits(sumOfDigits_global)
