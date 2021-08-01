"""
Cheezit's Brute force tool
The purpose of this tool is to compare alphabetical and random brute force attacks on passwords
@author: Braedon "Cheezit" Lyons
"""

# Imports
import itertools
import time
import pyautogui
import random

# Alphabetical brute force function
def alphabruteforce(password, chars, printData):
    start = time.time()
    attempts = 0
    for i in range(1, 9):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            if printData == True:
                print(letter)
            if letter == password:
                end = time.time()
                distance = end - start
                return (attempts, distance)

#random brute force function
def randombrute(password, chars, printData):
    guess_password = ""
    start = time.time()
    attempts = 0
    while (guess_password != password):
        attempts+=1
        guess_password = random.choices(chars, k=len(password))
        if printData == True:
            print(''.join([str(item) for item in guess_password]))
        if (guess_password == list(password)):
            end = time.time()
            distance = end - start
            return (attempts, distance)

#main testing function
def testing():
    print("Welcome to Cheezit's password cracking tool")
    print("The purpose of this tool is to compare alphabetical vs random brute forcing")
    print("")
    print("---------------------------------")

    #User inputs
    password = pyautogui.password("Enter a password : ")
    outputTries = pyautogui.prompt("Would you like to output passwords? (y/n)")
    if outputTries == "y":
        outputTries = True
    else:
        outputTries = False
    times = int(pyautogui.prompt("How many times would you like to try"))

    #variable set up
    alphaAvg = []
    randomAvg = []
    chars = "1234567890abcdefghijklmnopqrstuvwxyz"
    charsList = list(chars)

    #alphabetical crack
    print("Starting alphabetical crack...")
    for i in range(times):
        tries, timeAmount = alphabruteforce(password,chars, outputTries)
        print("Cracked the password " + password + " in " + str(tries) + " tries and " + str(timeAmount) + " seconds!")
        alphaAvg.append(timeAmount)

    print("")
    print("")
    #random crack
    print("Starting random crack...")
    for i in range(times):
        tries, timeAmount = randombrute(password, charsList, outputTries)
        print("Cracked the password " + password + " in " + str(tries) + " tries and " + str(timeAmount) + " seconds!")
        randomAvg.append(timeAmount)

    #data comparison
    print("")
    print("---------------------------------")
    print("Average time for alphabetical was " + str(sum(alphaAvg)/len(alphaAvg)) + " seconds")
    print("Average time for random was " + str(sum(randomAvg)/len(randomAvg)) + " seconds")

testing()


