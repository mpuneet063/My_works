print("Welcome to the game!")
print("Select a range")

#Selecting a range
F = input("From: ")
T = input("To: ")

#generating random number
import numpy as np
x = np.random.randint(F,T)

guess_count = 0

#matching the guesses
while True:
    g = int(input("Enter your guess: "))
    if g == x:
        print("Congrats! You won")
    else:
        print("Sorry, Try again")
        guess_count += 1
    if guess_count == 3:
        print("Out of attempts! The correct answer was: ", x)
        break

