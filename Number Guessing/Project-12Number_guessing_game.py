import random
from tabnanny import check
from Number_guessing_art import logo

easy_chances = 10
hard_chances = 5
end_game = False


def check_difficulty():
    difficulty = (input("Choose a difficulty, Type 'easy' or 'hard'\n")).lower()
    if  difficulty == 'easy':
        return easy_chances
    else:
        return hard_chances

def action(guess,chances,choose_num):
    if guess > choose_num:
        print("Too High!")
        print("Guess Again!")
        return (chances - 1)
    elif guess < choose_num:
        print("Too Low!")
        print("Guess Again!")
        return (chances - 1)
    elif guess == choose_num:
        print(f"You got it! The answer was {choose_num}")


def play_game():    
    print(logo)
    print("Welcome to the number-guessing game!")
    print("I am thinking of a number between 1 to 100")    
    choose_num = random.randint(1,100)
    chances = check_difficulty()

    guess = 0
    while guess != choose_num:
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        chances = action(guess, chances,choose_num)
        if chances == 0:
            print("YOu've run out of chances. You Lose!")
            return
        elif guess != choose_num:
            print("Guess again!")

    # guess = 0
    # while guess != choose_num:
    #     print(f"You have {chances} attempts remaining.")
    #     guess = int(input("Make a Guess: "))

    #     chances = action(guess, chances, choose_num)
    #     if chances == 0:
    #         print("You have run out of attempts. You Lose!")
    #         break

play_game()
    


    






