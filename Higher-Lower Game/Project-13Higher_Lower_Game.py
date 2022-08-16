from os import system
from pydoc import describe
from Higher_lower_art import logo, vs
from Higher_lower_list_of_data import data
import random

def select_choice():    
    return random.choice(data)


def format_choose(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return (f"{name}, a {description}, from {country}")

def play_game():
    final_score = 0
    end_game = False
    select_choice_a = select_choice()
    select_choice_b = select_choice()

    while not end_game: 
        # select_choice_a = select_choice_b
        # select_choice_b = select_choice()        
        print(logo)
        print(f"Compare A: {format_choose(select_choice_a)}")
        print(vs)
        print(f"Against B: {format_choose(select_choice_b)}")
        check = (input("Who has more followers? Type 'A' or 'B': ")).lower()
        if check == "a":
            if select_choice_a["follower_count"] < select_choice_b["follower_count"]:
                _ = system('cls')
                print(f"Sorry that's Wrong! Final Score: {final_score}")
                end_game = True
            else:
                select_choice_a = select_choice_b
                select_choice_b = select_choice()
                final_score += 1
                _ = system('cls')
                print(f"You're Right! Current Score = {final_score}")
                
        else:
            if select_choice_a["follower_count"] > select_choice_b["follower_count"]:
                _ = system('cls')             
                print(f"Sorry that's Wrong! Final Score: {final_score}")
                end_game = True
            else:
                select_choice_a = select_choice_b
                select_choice_b = select_choice()
                final_score += 1
                _ = system('cls')
                print(f"You're Right! Current Score = {final_score}")
        
    
play_game()

