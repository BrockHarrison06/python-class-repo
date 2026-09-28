from random import randrange

# Keep playing until the user chooses to stop.
play_again = "y"

while play_again == "y":
    # Generate a random number from a range of 0 to 10.
    # To adjust the range, edit the values within the parentheses.
    # The first number controls the lower bounds and the second controls the higher bounds.
    random_number = randrange(0, 10)

    # Explain the purpose of the game.
    print("Guess the random number in 5 tries!")

    # Counter to keep track of the number of guesses.
    guess_count = 0
    guessed_correctly = False

    # Allow the user a maximum of 5 guesses.
    while guess_count < 5:
        guess = int(input("Guess #" + str(guess_count + 1) + ". Enter your next guess: "))
        guess_count += 1

        # Check whether the user's guess is correct.
        if guess == random_number:
            print("You guessed the random number:", random_number)
            print("It took you", guess_count, "tries")
            guessed_correctly = True
            break
        else:
            # Give feedback when the guess is incorrect.
            print("Sorry, that is incorrect, please try again")

    # If all 5 guesses were used without a correct answer, the user loses.
    if guessed_correctly == False:
        print("Sorry, You lose! The number was:", random_number)

    # Ask whether the user wants to play again.
    play_again = input("Would you like to play again (y/n): ")
    play_again = play_again.lower()

    # Validate the response so only y or n is accepted.
    while play_again != "y" and play_again != "n":
        play_again = input("Please enter y or n: ")
        play_again = play_again.lower()

print("Completed by, Brock")
