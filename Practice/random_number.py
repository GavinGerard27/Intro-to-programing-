import random

def number_guesser():
    print("I'm thinking of a number between 1 and 1000.")
    secret_number = random.randint(1, 1000)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess "))
            attempts += 1

            if guess < secret_number:
                print(" Too low,Try again.")
            elif guess > secret_number:
                print(" Too high,Try again.")
            else:
                print(f" Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print(" Please enter a valid number.")
    with open("C:\Users\828387\Documents\Intro to program\Intro-to-programing-\Assignments\sample.txt", "a"):
        file.write("\n" + name + "," + str(attempts))
        file.close()
number_guesser()

