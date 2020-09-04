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
    |        /|\
    |      
    |
==================''', '''

   ______________
    |         |
    |         0
    |        /|\
    |        / 
==================''', '''

   ______________
    |         |
    |         0
    |        /|\
    |        / \
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


def get_words(word_list):
    # TODO: function to return word from selected word category
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

def game_status(missedLetters, correctLetters, secretWord):
    # TODO: function to return current game status or main UI
    print(hangman_pic)                                  ######***********