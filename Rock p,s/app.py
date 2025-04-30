import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def get_user_choice():
    while True:
        print_slow("\nEnter your choice (rock/paper/scissors) or 'q' to quit: ")
        choice = input().lower().strip()
        
        if choice in ['rock', 'paper', 'scissors', 'q']:
            return choice
        else:
            print_slow("Invalid choice! Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    score = {'user': 0, 'computer': 0, 'ties': 0}
    
    print_slow("\n=== Welcome to Rock, Paper, Scissors! ===")
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'q':
            break
            
        computer_choice = get_computer_choice()
        
        print_slow(f"\nYou chose: {user_choice}")
        print_slow(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print_slow(f"\n{result}")
        
        if result == "You win!":
            score['user'] += 1
        elif result == "Computer wins!":
            score['computer'] += 1
        else:
            score['ties'] += 1
        
        print_slow(f"\nScore - You: {score['user']} | Computer: {score['computer']} | Ties: {score['ties']}")

    print_slow("\n=== Final Score ===")
    print_slow(f"You: {score['user']}")
    print_slow(f"Computer: {score['computer']}")
    print_slow(f"Ties: {score['ties']}")
    print_slow("\nThanks for playing!")

if __name__ == "__main__":
    play_game()
