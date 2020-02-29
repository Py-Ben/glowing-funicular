import random

your_score = 0
comp_score = 0
tie_score = 0
match = 1
comp_options = ["paper", "rock", "scissors"]
play_again = "yes"
print('\n' * 100)
print('Welcome to PRS!')

while play_again.lower() in ("yes", "y"):
    print('--------------------------')
    print(f"***** Round {match} *****\n")
    user_choice = input("Paper, Rock, or Scissors? ")
    while user_choice.lower() not in {"paper", "rock", "scissors"}:
        print("Invalid selction. Please try again.")
        user_choice = input("Paper, Rock, or scissors? ")
        
    comp_play = random.choice(comp_options)
    print(f"The computer picked {comp_play.title()}")
    if user_choice.lower() == "paper" and comp_play == "rock":
        match = match + 1
        your_score = your_score + 1
        print("You Win!")
        print('--------------------------')
        print(f"You {your_score} - Computer {comp_score} - Tie {tie_score}")
        print('--------------------------')
        play_again = input("Want to play again? yes\\no ")
        while play_again.lower() not in {"yes", "no", "y", "n"}:
            print("Invalid response")
            play_again = input("Want to play again? yes\\no ")

    elif user_choice.lower() == "rock" and comp_play == "scissors":
        match = match + 1
        your_score = your_score + 1
        print("You Win!")
        print('--------------------------')
        print(f"You {your_score} - Computer {comp_score} - Tie {tie_score}")
        print('--------------------------')
        play_again = input("Want to play again? yes\\no ")
        while play_again.lower() not in {"yes", "no", "y", "n"}:
            print("Invalid response")
            play_again = input("Want to play again? yes\\no ")

    elif user_choice.lower() == "scissors" and comp_play == "paper":
        match = match + 1
        your_score = your_score + 1
        print("You Win!")
        print('--------------------------')
        print(f"You {your_score} - Computer {comp_score} - Tie {tie_score}")
        print('--------------------------')
        play_again = input("Want to play again? yes\\no ")
        while play_again.lower() not in {"yes", "no", "y", "n"}:
            print("Invalid response")
            play_again = input("Want to play again? yes\\no ")

    elif user_choice.lower() == comp_play:
        match = match + 1
        tie_score = tie_score + 1
        print("It's a tie!")
        print('--------------------------')
        print(f"You {your_score} - Computer {comp_score} - Tie {tie_score}")
        print('--------------------------')
        play_again = input("Want to play again? yes\\no ")
        while play_again.lower() not in {"yes", "no", "y", "n"}:
            print("Invalid response")
            play_again = input("Want to play again? yes\\no ")

    else:
        comp_score = comp_score + 1
        match = match + 1
        print("you lose :(")
        print('--------------------------')
        print(f"You {your_score} - Computer {comp_score} - Tie {tie_score}")
        print('--------------------------')
        play_again = input("Want to play again? yes\\no ")
        while play_again.lower() not in {"yes", "no", "y", "n"}:
            print("Invalid response")
            play_again = input("Want to play again? yes\\no ")
else:
    print("Thanks for playing!")