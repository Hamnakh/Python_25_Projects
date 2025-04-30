import random

def get_word():
    words = ['banana', 'apple', 'orange', 'mango', 'strawberry']
    return random.choice(words).lower()

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |      
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |      
           -
        """
    ]
    return stages[tries]

def play_hangman():
    word = get_word()
    word_letters = set(word)  # Letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # Letters guessed by the user
    
    lives = 6  # Total attempts

    print("\n🎉 Welcome to Hangman!")
    print(display_hangman(lives))  # Show initial hangman state

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        print(f'\n🔹 Lives left: {lives}')
        print('🔠 Used letters:', ' '.join(sorted(used_letters)))

        # Show current progress
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Word: ", ' '.join(word_list))

        user_letter = input("🔤 Guess a letter: ").lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("❌ Wrong guess!")
        
        elif user_letter in used_letters:
            print("⚠️ This letter is already guessed. Choose another.")

        else:
            print("🚨 Invalid input! Please enter a valid letter.")

        print(display_hangman(lives))  # Update hangman after guess

    # Game over conditions
    if lives == 0:
        print("\n💀 Game Over! The correct word was:", word)
    else:
        print("\n🎉 Congratulations! You guessed the word:", word)

if __name__ == '__main__':
    play_hangman()
