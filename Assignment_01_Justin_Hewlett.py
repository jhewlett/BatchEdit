'''
Justin Hewlett
CS 3430
Assignment 1

A python program to approximate roots for a function.
Uses the Newton-Raphson method to approximate.
'''

#Takes an intial guess, a function, and the derivative of the function
#Recursively makes closer and closer guesses until the same guess is made
#twice in a row (rounded to the 10th decimal place).
#Returns the final approximation
def newton_raphson(guess, f, dfdx):
    print guess
    next_guess = get_next_guess(guess, f, dfdx)
    if round(next_guess, 10) == round(guess, 10):
        #Our guess is close enough. Print and return the final guess.
        print next_guess
        return next_guess
    else:
        #Recursively guess again
        newton_raphson(next_guess, f, dfdx)

#Helper function to compute the next guess based on the previous guess
def get_next_guess(guess, f, dfdx):
    return guess - f(guess)/dfdx(guess);

#This is a sample function and its derivative for testing
def f1(x):
    return x * x * x - (4 * x) + 5

def dfdx1(x):
    return 3 * x * x - 4

