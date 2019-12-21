import string
from words import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    return False

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    
    import string
    letters_left = string.ascii_lowercase 
    #ascii_lowercase is a pre-initialized string used as string constant,
    #will give the lowercase letters ‘abcdefghijklmnopqrstuvwxyz’.

    return letters_left

def hangman(secret_word):

    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    while (True):
      letters_guessed = []
      
      available_letters = get_available_letters(letters_guessed)
      print ("Available letters: " + available_letters)

      guess = input("Please guess a letter: ")
      letter = guess.lower()

      if letter in secret_word:
          letters_guessed.append(letter)
          print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
          print ("")

          if is_word_guessed(secret_word, letters_guessed) == True:
              print (" * * Congratulations, you won! * * ")
              print ("")
              break
      else:
          print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
          letters_guessed.append(letter)
          print ("")
    
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)