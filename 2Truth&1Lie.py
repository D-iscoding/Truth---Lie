import random

print("TWO TRUTH AND A LIE!")

facts = [
    "I love pizza.",
    "I have a pet tiger.",
    "I can speak three languages."
]

answers = [True, False, True]
correct_guesses = 0

for turn in range(3):
    fact_number = random.randint(0, 3)
    print("Fact " + str(turn + 1) + ": " + facts[fact_number])

    guess = input("Do you think this is a truth or a lie? (Enter 'y' or 'n'): ").lower()

    if (guess == 'y' and answers[fact_number] == True) or (guess == 'n' and answers[fact_number] == False):
        print("Correct!")
        correct_guesses += 1
    else:
        print("Incorrect!")

print("You got " + str(correct_guesses) + " out of 3 correct!")
print("GAME OVER!")
