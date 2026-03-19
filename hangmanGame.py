import random
# Hangman Game

# list of word 
words = ["python", "django","javascript", "react", "developer"]

# choose a random word from existing list
word = random.choice(words)

# declare list for store guessed word
guessed_letters = []

# flag for user attempts 
attempts = 6

# create hidden word like (__ABC)
display_word = ["_"] * len(word)

# print game descriptions
print("Welcome to the Hangman Game!")
print("Guess the word, letter by letter.")
print("You have 6 attempts.\n")

# loop through in game
while attempts > 0 and "_" in display_word:
    
    print("word: "," ".join(display_word))
    print(f"Wrong attempts left: {attempts}")
    
    # take input from user and store in guess variable
    guess = input(f"Enter a letter: ").lower()
    
    # checked weather is guess is correct
    if guess in guessed_letters:
        
        print(f"You guessed the correct word.\n")
        # if user guess word continue
        
        continue
    
    # append guess word in guessed_letters
    guessed_letters.append(guess)
    
    # checked weather guess is correct
    if guess in word:
        print("Your guess is Correct!")
        
        # update display word
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!\n")
        attempts -= 1
                
# result of game
if "_" not in display_word:
    print("Congratulation! you win the game.")
    print("The word is", word)
    
else:
    print("Game over!")
    print("The word is", word)