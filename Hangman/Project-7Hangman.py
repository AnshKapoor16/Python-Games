import random
import hangman_art
from hangman_words import word_list

print(hangman_art.logo)
print(hangman_art.stages[6])

word = random.choice(word_list)
print(f"Pssst.. The word is {word}")

dash_list = []
for letter in word:
    dash_list.append("_")
print(dash_list)

lives = 6

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter.\n").lower()
    if guess in dash_list:
        print(f"You have already guessed the letter {guess}")
    for position in range(len(word)):
        if word[position] == guess:
            dash_list[position] = word[position]
    if guess not in word:
        print(f"You have guessed the letter {guess} which is not in the word")
        lives -= 1
    print(dash_list)
    print(hangman_art.stages[lives])

    if "_" not in dash_list:
        end_of_game = True
        print("You Won!")
    
    if lives == 0:
        end_of_game = True
        print("You lose!")






