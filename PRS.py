import random

comp_options = ["paper", "rock", "scissors"]
play_again = "yes"

while play_again == "yes":
    user_choice = input("Paper, Rock, or scissors? ")
    while user_choice.lower() not in {"paper", "rock", "scissors"}:
        print("Invalid selction. Please try again.")
        user_choice = input("Paper, Rock, or scissors? ")

    comp_play = random.choice(comp_options)
    
    if user_choice.lower() == "paper" and comp_play == "rock":
        print("You Win!")
        play_again = input("Want to play again? yes\\no ")
        while play_again.lower() not in {"yes", "no"}:
            print("Invalid response")
            play_again = input("Want to play again? yes\\no ")

    elif user_choice.lower() == "rock" and comp_play == "scissors":
        print("You Win!")
        play_again = input("Want to play again? yes\\no ")
        while play_again.lower() not in {"yes", "no"}:
            print("Invalid response")
            play_again = input("Want to play again? yes\\no ")

    elif user_choice.lower() == "scissors" and comp_play == "paper":
        print("You Win!")
        play_again = input("Want to play again? yes\\no ")
        while play_again.lower() not in {"yes", "no"}:
            print("Invalid response")
            play_again = input("Want to play again? yes\\no ")

    elif user_choice.lower() == comp_play:
        print("It's a tie!")
        play_again = input("Want to play again? yes\\no ")
        while play_again.lower() not in {"yes", "no"}:
            print("Invalid response")
            play_again = input("Want to play again? yes\\no ")

    else:
        print("you lose :(")
        play_again = input("Want to play again? yes\\no ")
        while play_again.lower() not in {"yes", "no"}:
            print("Invalid response")
            play_again = input("Want to play again? yes\\no ")
    

