
import random
print("Welcome to the Rock Paper Scissors Game!")
st=int(input("Press 5 to start the game"))

if st==5:
    while True:
        print("Great! Let's play!")
        print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
        options=["rock","paper","scissors"]
        player_choice=input("Enter your choice (rock/paper/scissors): ").lower().strip()
        print("Player choosen:",player_choice)
        computer_choice=random.choice(options)
        print("Computer choosen:",computer_choice)
        if player_choice==computer_choice:
            print("It's a tie!")
            play_again=input("Do you want to play again? (y/n): ").lower().strip()
            if play_again != 'y':
                print("Thanks for playing! Goodbye!")
                break
        elif(player_choice=="rock" and computer_choice=="scissors" or player_choice=="scissors" and computer_choice=="paper" or player_choice=="paper" and computer_choice=="rock"):
            print("Congratulations! You win!")
            play_again=input("Do you want to play again? (y/n): ").lower().strip()
            if play_again != 'y':
                print("Thanks for playing! Goodbye!")
                break
        else:
            print("Sorry! Computer wins!")
            play_again=input("Do you want to play again? (y/n): ").lower().strip()
            if play_again != 'y':
                print("Thanks for playing! Goodbye!")
                break
else:
    print("Invalid input. Please press 5 to start the game.")
