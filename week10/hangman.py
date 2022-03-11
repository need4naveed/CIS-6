import random
hangman_visual = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
  |\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  ______
 /      \  RIP HANGMAN
| X   X  |
|   __   |
 \______/''', '''
  ______
 /      \  YOU SAVED HIM! 
|  ^  -  | NICE VOCABULARY!
|  \__/  |
 \______/''']

#list of words to choose from
words = '''cabbage sheep brass rustic canvass tomatoes paper sweater stomach erase kitten flavor escape
crayon bread tiger groovy brother oranges pencil square potato elbow vacation aquatic'''.split()

def gameBoard(missedLetters, correctLetters, secretWord): #function to display the board of the game
     print(hangman_visual[len(missedLetters)]) #prints hangman visual
     print('\nMissed letters:', end=' ')
     for letter in missedLetters: #prints missed letters seperated by spacea
         print(letter, end=' ')
     print()

     blanks = '_' * len(secretWord) #makes blank word the size of secret word
     for i in range(len(secretWord)): 
         if secretWord[i] in correctLetters:
             blanks = blanks[:i] + secretWord[i] + blanks[i+1:] #replaces blanks with correct guesses

     for letter in blanks: #prints the secret word with spaces seperating the underscores
         print(letter, end=' ')
     print()

def checkGuess(oldGuess): #checks the guess to make sure it is a valid character
     while True:
         guess = input('Guess a letter: ')
         guess = guess.lower()
         if guess in oldGuess: #checks if guess have been done already
             print('You already guessed that letter.')
         elif len(guess) != 1: #checks if they enter more or less than 1 letter
             print('Please enter a single letter.')
         elif guess not in 'abcdefghijklmnopqrstuvwxyz': #checks if user entered a character other than a letter
             print('Please enter a letter.')
         else:
             return guess
            
def randoWord(wordList):    #returns a random word from the list of words
     guessWord = random.randint(0, len(wordList) - 1)
     return wordList[guessWord]

print('Use your vocabulary skills and save Mr.Hangman from his doom') #added plot, lore enhances user experience    
print('H A N G M A N')
gameEnd = False
missedLetters = ''
correctLetters = ''
secretWord = randoWord(words)

while True:
     gameBoard(missedLetters, correctLetters, secretWord) #display board
     guess = checkGuess(missedLetters + correctLetters) #gets new guess
     if guess in secretWord:
         correctLetters = correctLetters + guess #adds correct guesses to correct letters variable

         allLetters = True 
         for i in range(len(secretWord)):
             if secretWord[i] not in correctLetters: #checks for win by seeing if every letter matches, returns false if a letter does not match
                 allLetters = False
                 break
         if allLetters:
             print('You got it! The secret word was "' + secretWord + '"!')
             print(hangman_visual[8]) #win screen
             gameEnd = True
     else:
         missedLetters = missedLetters + guess #adds missed guesses to missed letter variable

         if len(missedLetters) == len(hangman_visual) - 3: #displays loss if guesses exceeds number of guesses
             gameBoard(missedLetters, correctLetters, secretWord)
             print('Out of guesses!')
             print('The secret word was "', secretWord, '"')
             print('You had ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses')
             print(hangman_visual[7]) #loss screen
             gameEnd = True

     if gameEnd: #asks if they want to play again if the game is finished
         replay = input('\nDo you want to play again? (y/n)\n')
         if replay.startswith('y'): #replays the game if user enters anything starting with 'y'
             print('H A N G M A N')
             gameEnd = False
             missedLetters = ''
             correctLetters = ''
             secretWord = randoWord(words)
         else:
             break
