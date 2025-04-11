import random

def play_guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("\n🎉 Welcome to the Guess the Number Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it correctly!")

    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = input("\nEnter your guess: ")
            
            # Check if input is a valid number
            if not guess.isdigit():
                print("🚨 Invalid input! Please enter a number between 1 and 100.")
                continue

            guess = int(guess)
            
            if guess < 1 or guess > 100:
                print("🚨 Out of range! Please enter a number between 1 and 100.")
                continue

            attempts += 1

            # Check the guess
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts! 🎯")
                return
            elif guess < secret_number:
                print("🔻 Too low! Try a higher number.")
            else:
                print("🔺 Too high! Try a lower number.")
            
            # Show remaining attempts
            print(f"⚡ Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("🚨 Error! Please enter a valid number.")

    print(f"\n❌ Game Over! The correct number was {secret_number}.")

if __name__ == "__main__":
    while True:
        play_guess_number()
        play_again = input("\n🔄 Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\n👋 Thanks for playing! See you next time! 🎮")
            break
