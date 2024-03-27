import random
from hangman_art import logo
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
lives = 6
print(logo)
print(f'Pssst, the solution is {chosen_word}.')


display = []
for letter in chosen_word:
    display.append("_")

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for i in range(0, len(display)):
         if guess == chosen_word[i]:
            display[i] = guess
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
    if '_' not in display:
        end_of_game = True
        print("You won")
    if lives == 0:
        print("You lost")
        end_of_game = True

print(display)