import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Let's play a game of Rock, Paper and Scissors!")
choice = int(input("What do you choose?  0-Rock, 1-Paper, 2-Scissor\n"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Try Again!")

print("Computer Chose:")
game = [rock, paper, scissors]
result = random.randint(0,2)
print(game[result])

if choice == 0:
    if result == 0:
        print("It's a Tie!")
    elif result == 1:
        print("You Lost!")
    elif result == 2:
        print("You Won!")
if choice == 1:
    if result == 0:
        print("You Won!")
    elif result == 1:
        print("It's a Tie!")
    elif result == 2:
        print("You Lost!")
if choice == 2:
    if result == 0:
        print("You Lost!")
    elif result == 1:
        print("You Won!")
    elif result == 2:
        print("It's a Tie!")



