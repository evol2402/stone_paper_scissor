from inventory import scissors, paper, title, stone
from time import sleep
from random import choice
from datetime import datetime

# List of valid choices for the player
correct_list = ['s', 'c', 'p']

# Dictionary to map the player's input to the respective choice name
correct_dict = {
    "s": stone,
    "c": scissors,
    "p": paper
}

game_is_on = True  # Variable to control the game loop
user_score = 0  # Initialize score to 0
computer_score = 0

# Print the title and welcome message
print(title)
# Display the game rules
print("\nGAME RULES:")
print("1. You will be playing against the computer.")
print("2. Choose one of the following options:")
print("   - 's' for Stone")
print("   - 'p' for Paper")
print("   - 'c' for Scissors")
print("3. The winner is determined as follows:")
print("   - Stone beats Scissors")
print("   - Scissors beats Paper")
print("   - Paper beats Stone")
print("4. If both choices are the same, it's a tie!")
print("\nGood luck and have fun!\n")

print("Let the game begin!!!!!!!")


# Get the player's name and format it
player = str(input("Enter Player Name:")).title()
print(f'{player}, make your choice!!!!!')

# Start the game loop
while game_is_on:
    # Ask for player's choice and convert it to lowercase
    player_choice = input(f'Press "s" for stone\nPress "p" for paper\nPress "c" for scissors\nChoice:').lower()

    # Check if the player made a valid choice
    if player_choice not in correct_list:
        print("Invalid choice, make your selection again.")
    else:
        # Introduce a delay before showing the choices
        print("So here we go!!!!!")
        print("Stone, ", end="")
        sleep(0.5)
        print("Paper, ", end="")
        sleep(0.5)
        print("and Scissors\n")
        sleep(0.5)

        # Display the player's choice
        print(f'{player} Choice: {correct_dict[player_choice]}\n')

        # Computer makes a random choice from the valid list
        computer_choice = choice(correct_list)
        print(f"Computer chose: {correct_dict[computer_choice]}")

        # Determine the outcome of the round
        if player_choice == computer_choice:
            print("It's a tie!")
            print(f'Computer Score:{computer_score}\n{player} Score: {user_score}\n')
        elif (player_choice == 's' and computer_choice == 'c') or \
                (player_choice == 'p' and computer_choice == 's') or \
                (player_choice == 'c' and computer_choice == 'p'):
            print(f"{player} wins!")
            user_score += 1  # Increment the player's score when they win
            print(f'Computer Score:{computer_score}\n{player} Score: {user_score}\n')
        else:
            print("Computer wins!")
            computer_score += 1
            print(f'Computer Score:{computer_score}\n{player} Score: {user_score}\n')

        # Ensure the user enters 'y' or 'n' for playing again
        while True:
            play_again = input("Want to play again? (y/n): ").lower()
            if play_again == 'y' or play_again == 'n':
                break  # Exit the loop if valid input is provided
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

        if play_again != 'y':
            game_is_on = False  # End the game loop
            print("Thanks for playing!")

            # Get the current date and time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Write the player's username and score to 'result.txt'
            with open('result.txt', 'a') as file:
                file.write(f"Username: {player}\nScore: {score}\nDate and Time: {current_time}")
            print(f"Your score has been saved to 'result.txt'.")
