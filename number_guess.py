import random

def number_guessing_game():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 50. Can you guess it?")

    # Random number between 1–50
    secret_number = random.randint(1, 50)
    attempts = 0
    guess = 0

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        except ValueError:
            print("❌ Please enter a valid number!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
