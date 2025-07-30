#intitialilzing the game
import random
words = ['apple', 'mango', 'banana', 'orange','lichi','pineapple','papaya','lemon','pomegranate']
word = random.choice(words)

#welcoming the gamer
print("I am the HANGMAN!!")
print("Guess the right word or prepare to be hanged")

#number of guesses
turns = int(len(word)) + 2
print ("You have", turns, "attempts")

#starting the game
print("Guess the characters")
guesses = ''

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("\nYou Win. The HANGMAN lets you go.")
        break

    guess = input("Enter your guess: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print('GAME OVER! Correct word was:', word)
            print('NOW YOU SHALL BE HANGED!!')