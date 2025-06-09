import random

num = random.randint(1, 100)
tries=0
guessed = False

while guessed == False:
    guess = int(input("Guess the number: "))
    if guess > 100 or guess < 1:
        print("That's not a valid guess. Please guess a number between 1-100.")
    elif guess == num:
        guessed = True
        tries+=1
        print(f"Congrats! You have guessed the number in {tries} tries!")
    elif guess > num:
        print("Lower")
        tries+=1
    elif guess < num:
        print("Higher")
        tries+=1