import random

play_again = "yes"
user_score = 0
comp_score = 0

while play_again in ("yes", "y"):
    print('\n' * 100)
    try_count = 0
    comp_num = random.randint(1, 10)
    print("Welcome to Bella's number game!")
    print("-------------------------------\n")
    while try_count < 3:
        user_num = int(input('Enter your number 1 - 10: '))
        if user_num == comp_num:
            try_count = try_count + 1
            break
        elif user_num > comp_num:
            try_count = try_count + 1
            print("You guessed too high!\n")
        elif user_num < comp_num:
            try_count = try_count + 1
            print('You guessed too low!\n')
    if user_num == comp_num:
        print(f'\nThe computer picked {comp_num}')        
        print('You win!')
        print("-------------------------------\n")
        user_score = user_score + 1
        print(f"You {user_score} - Computer {comp_score}")
        print("-------------------------------\n")
        play_again = input('Want to play again? Yes/No? ')
        while play_again.lower() not in {"yes", "no", "y", "n"}:
            print("Invalid response")
            play_again = input("Want to play again? Yes/No?  ")
    else:
        print(f'\nThe computer picked {comp_num}')
        print('You lose')
        print("-------------------------------\n")
        comp_score = comp_score + 1
        print(f"You {user_score} - Computer {comp_score}")
        print("-------------------------------\n")
        play_again = input('Want to play again? Yes/No? ')
        while play_again.lower() not in {"yes", "no", "y", "n"}:
            print("Invalid response")
            play_again = input("Want to play again? Yes/No?  ")


