import random
import sys

def main():
    # welcome message
    print("Welcome to Coomber's Number Guessing Game!")
    
    # infinite loop for the game, which will only break when the user chooses to quit
    while True:
        # get user input
        user_input = input("Enter your guess (1-100) or 'q' to quit: ")
        if user_input.lower() == 'q':
            print("See you next time")
            break
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input, please enter a number between 1 and 100.")
            continue
        
        if guess < 1 or guess > 100:
            print("Invalid input, please enter a number between 1 and 100.")
            continue
        
        number_to_guess = random.randint(1, 100)
        attempts = 0
        
        while True:
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
                guess = int(input("Enter your guess (1-100): "))
            elif guess > number_to_guess:
                print("Too high! Try again.")
                guess = int(input("Enter your guess (1-100): "))
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                play_again()


def play_again():
    # ask user if they want to play again
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            main()
        elif play_again == 'n':
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()

