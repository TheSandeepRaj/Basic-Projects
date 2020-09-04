# https://en.wikipedia.org/wiki/Hangman_(game)
# Layout - Keypad, Word in progress, 
# ToDOs: Ask for how many guess u  want, guesses remain, 
#       prev guess
#commonly used letters — E, S, T, M, and N 

import random
hangman_pic = ['''

   ______________
    |         |
    |         
    |        
    |        
    |
==================''', '''

   ______________
    |         |
    |         0
    |  
    |  
    |
==================''', '''

   ______________
    |         |
    |         0
    |         |
    |   
    |
==================''', '''

   ______________
    |         |
    |         0
    |        /|
    |        
    |
==================''', '''

   ______________
    |         |
    |         0
    |        /|\\
    |      
    |
==================''', '''

   ______________
    |         |
    |         0
    |        /|\\
    |        / 
    |
==================''', '''

   ______________
    |         |
    |         0
    |        /|\\
    |        / \\
    |
==================''', '''

''']

# List of word list based on category 
words_animal = ('Ant Baboon Badger Bat Bear Beaver Camel Cat Clam Cobra Cougar Coyote Crow'
                'Deer Dog Donkey Duck Eagle Ferret Fox Frog Goat Goose Hawk Lion Lizard Llama'
                'Mole Monkey Moose Mouse Mule Newt Otter Owl Panda Parrot Pigeon Python Rabbit'
                'Ram Rat Raven Rhino Salmon Seal Shark Sheep Skunk Sloth Snake Spider Stork'
                'Swan Tiger Toad Trout Turkey Turtle Weasel Whale Wolf Wombat Zebra').split()

# words_eng = ('Instantaneous Heavily Moderately Essential Feature Consumption Dissipation'
#             'Actuate Prescribed Designate Overwhelmed Tremendous Inconsequential Accumulation'
#             'Intrinsic Diffuse Bias Convey Constraints Monetary Catastrophe').split()

# words_easy = 

# words_medium =

# words_hard = 

# words_expert =


def secrect_word(word_list):
    # TODO: function to return secrect word from selected word category
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

def game_status(missed_letters, correct_etters, secret_word):
    # TODO: function to return current game status or main UI
    print(hangman_pic[len(missed_letters)] +'\n' )
    
    # TODO: guess left 
    guess_left = 6 - len(missed_letter)
    print('Guess Left: ' + str(guess_left), end='\t')

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter)

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):       # replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:                   # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()




print(hangman_pic[5] +'\n')