import random

# Function to get the computer's choice
def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

# Function to display results
def display_results(user, computer, result):
    print(f"Your choice: {user}")
    print(f"Computer's choice: {computer}")
    
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

# Main game loop
def play_game():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Choose 'rock', 'paper', or 'scissors'.")
    
    while True:
        # Get user input
        user = input("Enter your choice (rock, paper, scissors): ").lower()
        
        # Validate user input
        if user not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please enter 'rock', 'paper', or 'scissors'.")
            continue
        
        # Get computer's choice
        computer = computer_choice()
        
        # Determine winner
        result = determine_winner(user, computer)
        
        # Update scores
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        
        # Display results and scores
        display_results(user, computer, result)
        print(f"Score: You - {user_score} | Computer - {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Final scores:")
            print(f"Final Score: You - {user_score} | Computer - {computer_score}")
            break

# Start the game
play_game()
