# https://en.wikipedia.org/wiki/Hangman_(game)
# ToDOs: Ask for how many guess u  want, guesses remain, 
#commonly used letters — E, S, T, M, and N 

import random

# Variable name 'HANGMAN_PICS' is all CAPS since this is the programming convention for "constant variables".
HANGMAN_PICS = ['''

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
words_animal = ('Ant Baboon Badger Bat Bear Beaver Camel Cat Clam Cobra Cougar Coyote Crow '
                'Deer Dog Donkey Duck Eagle Ferret Fox Frog Goat Goose Hawk Lion Lizard Llama '
                'Mole Monkey Moose Mouse Mule Newt Otter Owl Panda Parrot Pigeon Python Rabbit '
                'Ram Rat Raven Rhino Salmon Seal Shark Sheep Skunk Sloth Snake Spider Stork'
                'Swan Tiger Toad Trout Turkey Turtle Weasel Whale Wolf Wombat Zebra').split()

# words_eng = ('Instantaneous Heavily Moderately Essential Feature Consumption Dissipation'
#             'Actuate Prescribed Designate Overwhelmed Tremendous Inconsequential Accumulation'
#             'Intrinsic Diffuse Bias Convey Constraints Monetary Catastrophe').split()

# words_easy = 

# words_medium =

# words_hard = 

# words_expert =

words = words_animal


def get_secret_word(word_list):
    # TODO: function to return secrect word from selected word category
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

def get_game_status(HANGMAN_PICS, missed_letters, correct_letters, secret_word):
    # TODO: function to return current game status or main UI
    print(HANGMAN_PICS[len(missed_letters)] +'\n' )
    
    # TODO: guess left 
    guess_left = 7 - len(missed_letters)
    print('Guess Left: ' + str(guess_left), end='\t')

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')          #   end=' ' to show 'asdf' as 'a s d f'   if that
    print()

    blanks = '_' * len(secret_word)         # for 5 word letter blanks = '_____'

    for i in range(len(secret_word)):        #   replace blanks with correctly guessed letters
        if secret_word[i].lower() in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:                   # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def get_guess(already_guessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


# Main part starts here
print('WELCOME to H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = get_secret_word(words)
game_is_done = False

#debug
print(secret_word)

while True:
    get_game_status(HANGMAN_PICS, missed_letters, correct_letters, secret_word)

    # Let the player type in a letter.
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word.lower():
        correct_letters += guess

        # Check if the player has won
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Yes! The secret word is "' + secret_word + '"! You have won!')
            game_is_done = True
    else:
        missed_letters += guess

        # Check if player has guessed too many times and lost
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            get_game_status(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
            print('After ' + str(len(missed_letters)) + ' missed guesses and '
                     + str(len(correct_letters)) + ' correct guesses, the word was "' + secret_word.upper() + '"')
            game_is_done = True

    # Ask the player if they want to play again (but only if the game is done).
    if game_is_done:
        play_again = input('Do you want to play again? (yes or no)\n').lower().startswith('y')
        while play_again:
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = get_secret_word(words)
        break
