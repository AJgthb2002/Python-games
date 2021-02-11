import random
from os import system, name 
from hangman_words import word_list
from hangman_art import logo, stages

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 

chosen_word= random.choice(word_list)

print(logo)
print()
display=['_' for letter in chosen_word]
print(f"{' '.join(display)}")
print()

end_of_game=False
lives_left=6

while (not end_of_game):
    guess= input("Guess a letter: ").lower()
    clear()
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position]== guess:
                display[position]=guess
    else:
        lives_left-=1
        print(f"The letter {guess} is not in the word. You lost a life.")
           
    print(f"{' '.join(display)}")
    print()
    if ('_' not in display) or lives_left==0:
        end_of_game= True
    print(stages[lives_left])    

if lives_left==0:
    print(f"Sorry, you lost! The correct word was {chosen_word}")
else:
    print("Congratulations! You won.")    