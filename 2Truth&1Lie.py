import random

# Intro
print("2 TRUTHS AND A LIE")

# 2 Truths and a lie
facts = {
    "I can speak four different languages", # Lie
    # You need 3 facts
}

# Ask if the fact is true or falsh 
guess = input("Is this fact Truth or False? (T/F)").lower()

# Check player's guess
if guess == 'T' and random_fact != "I can speak four different languages.": # type: ignore
    print("Correct!")
elif guess == 'F' and random_fact != "I can speak four different languages.": # type: ignore
    print ("Correct!")
else:
    print("Incorrect!")

# Show results
print(f"/nYou got {correct_guesses} out of 1 correct!") # type: ignore

# Play the game again
play_again = input("Play Again? (Y/N): ").lower()